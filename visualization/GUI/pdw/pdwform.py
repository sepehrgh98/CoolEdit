import os
import random
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QLabel
from visualization.pdw.Channel.channel import Channel
from visualization.Radar.radarcontroller import RadarController
from visualization.GUI.pdw.pdwtools import PDWToolsForm
from visualization.GUI.pdw.datainformationform import DataInformationForm
from visualization.visualizationparams import ChannelUnit, DataPacket, FeedMood
from visualization.GUI.pdw.subplotwidget import SubPlotWidget
from visualization.GUI.progressdialog import ProgressDialog
from visualization.pdw.Channel.multichannel import MultiChannels
from visualization.visualizationparams import ProgressType
from visualization.GUI.defaultview.defaultview import DefaultView
from visualization.GUI.pdw.review import PDWReviewForm
from visualization.GUI.pdw.exportwindow import PDWExprtWindow



Form = uic.loadUiType(os.path.join(os.getcwd(), 'visualization', 'GUI', 'pdw', 'pdwui.ui'))[0]

class PDWForm(QMainWindow, Form):
    filePathChanged = pyqtSignal(str)
    selectDataRequested = pyqtSignal(tuple) # time range
    channelsSettedUp = pyqtSignal()
    clearRequested = pyqtSignal()
    deleteSelectedRequested = pyqtSignal(list) # list of tuples

    def __init__(self):
        super(PDWForm, self).__init__()
        self.setupUi(self)

        # widgets
        self.toolsWidget = PDWToolsForm()
        self.dataInfoWidget = DataInformationForm()
        self.reviewWidget = PDWReviewForm()
        self.subPlotsWidget = SubPlotWidget()
        self.radar_controller = RadarController()
        self.progress = ProgressDialog(self)
        self.default_view = DefaultView(icon_path = 
                            os.path.join(os.getcwd(), 'visualization', 'Resources', 'icons', 'main.png')
                            , text='Offline')
        self.export_window = PDWExprtWindow()

        # add widgets
        self.leftFrameLayout.addWidget(self.toolsWidget)
        self.dataInfoLayout.addWidget(self.dataInfoWidget)
        # self.reviewLayout.addWidget(self.reviewWidget)
        self.plotLayout.addWidget(self.default_view)


        # variables
        self.fig = self.subPlotsWidget.get_figure()
        self.canvas = self.fig.canvas
        self.hist_fig = self.subPlotsWidget.get_hist_figure()
        self.hist_canvas = self.hist_fig.canvas
        self.channels = []
        self.data_header = None
        self.radars = []
        self.feedMood = FeedMood.main_data
        self.omni_df_show_together = True
        self.plot_colors = ["#ADD8E6", "#A8F484", "#E5AAFE", "#F5ADA0", "#6D73F4"]
        self.number_of_fed_channels = 0

        # nav
        self.navbar = self.subPlotsWidget.get_nav_tool()

        # progress
        self.progress.setWindowTitle("File in Process ...")
        self.progress.setWindowModality(Qt.WindowModal)

        # initialization
        self.setup_connections()

    def setup_connections(self):
        # tool widget connections
        self.toolsWidget.filePathChanged.connect(self.on_filePathChanged)
        self.toolsWidget.filePathChanged.connect(self.dataInfoWidget.set_file_name)
        self.toolsWidget.selectBtnPressed.connect(self.subPlotsWidget.enable_select_action)
        self.toolsWidget.zoomRequested.connect(self.subPlotsWidget.enable_zoom_action)
        self.toolsWidget.panRequested.connect(self.subPlotsWidget.enable_pan_action)
        self.toolsWidget.selectAllRequested.connect(self.all_select_handle)
        self.toolsWidget.exportRequested.connect(self.export_process)
        self.toolsWidget.deleteSelectedRequested.connect(self.on_deleteSelectedReq)
        self.toolsWidget.radarRequested.connect(self.radar_controller.initialize_new_radar)
        self.toolsWidget.concatListIsReady.connect(self.handle_channel_concatination)
        self.toolsWidget.deselectAllRequested.connect(self.subPlotsWidget.unselectAllRequested)
        self.toolsWidget.clearRequested.connect(self.radar_controller.clear)
        self.toolsWidget.clearRequested.connect(self.subPlotsWidget.clear)
        self.toolsWidget.clearRequested.connect(self.on_clearRequested)
        self.toolsWidget.resetZoomRequested.connect(self.reset_zoom)
        # sub plot widget connections
        self.subPlotsWidget.selectionRangeHasBeenSet.connect(self.set_selection_area)
        self.subPlotsWidget.unselectAllRequested.connect(self.do_unselect_all)
        self.subPlotsWidget.unselectAllRequested.connect(self.radar_controller.reset)
        self.subPlotsWidget.unselectSpecialArea.connect(self.do_unselect_special_area)
        # default view widget connections
        self.default_view.filePathChanged.connect(self.on_filePathChanged)
        # self connections
        self.channelsSettedUp.connect(self.subPlotsWidget.setup_rect)
        self.channelsSettedUp.connect(self.subPlotsWidget.set_fig_size)



    @pyqtSlot(dict)
    def setup_channels(self, header):
        self.data_header = header
        if not self.radar_controller.channels_defined():
            self.radar_controller.setup_channel(header)
            self.toolsWidget.setup_channel(header)
        axs = self.fig.subplots(len(header.items()), 1, sharex='all')
        hist_axs = self.hist_fig.subplots(len(header.items()), 1)
        ch_counter = 0
        for _id, _info in header.items():
            ch = Channel(_id, _info[0], _info[1], axs[ch_counter], self.canvas, hist_axs[ch_counter], self.hist_canvas)
            ch.setup_style()
            self.channels.append(ch)
            ch_counter += 1
        self.channels[-1].set_x_tick("time"+"("+ ChannelUnit['TOA']+")")
        self.start_progress()
        self.channelsSettedUp.emit()
        self.canvas.draw()

    @pyqtSlot(DataPacket)
    def feed(self, data_packet):
        total_size=0
        select_size=0
        for channel in self.channels:
            current_channel = None
            if channel.is_multiple():
                exist_count = channel.ids.count(data_packet.id)
                if exist_count > 0:
                    current_channel = channel
            else:
                if channel.id == data_packet.id:
                    current_channel = channel
            if current_channel:
                if self.feedMood == FeedMood.main_data:
                    self.reviewWidget.feed(data_packet, mood="initilize")
                    current_channel.feed(data_packet.key, data_packet.data, random.choice(self.plot_colors), mood="initilize")
                    total_size += len(data_packet.key)
                    self.number_of_fed_channels += 1
                    self.feed_progressbar({ProgressType.visualizer:self.number_of_fed_channels/len(self.channels)})
                elif self.feedMood == FeedMood.select:
                    self.radar_controller.feed(data_packet)
                    current_channel.feed(data_packet.key, data_packet.data, "red", mood="selection")
                    self.reviewWidget.feed_marked(data_packet)
                    select_size += len(data_packet.key)
                    self.export_window.feed(data_packet)
                    break

        if self.feedMood == FeedMood.main_data:
            self.dataInfoWidget.set_total_data_size(total_size)
        else:
            self.dataInfoWidget.set_select_data_size(select_size)
                   

        self.canvas.draw()
        self.canvas.flush_events()
        self.hist_canvas.draw()
        self.hist_canvas.flush_events()
        
    @pyqtSlot(tuple)
    def set_selection_area(self, x_range=(-1,)):
        self.feedMood = FeedMood.select
        self.selectDataRequested.emit(x_range)

    @pyqtSlot()
    def do_unselect_all(self):
        self.feedMood = FeedMood.main_data
        self.dataInfoWidget.set_select_data_size(0)
        self.subPlotsWidget.clear_selection_area()
        self.reviewWidget.unmark_all()
        for channel in self.channels:
            channel.cancel_selection_all()

    @pyqtSlot(tuple)
    def do_unselect_special_area(self, area):
        self.reviewWidget.unmark(area)
        for channel in self.channels:
            channel.cancel_selection(area)

    def start_progress(self):
        self.progress.show()

    def all_select_handle(self):
        self.set_selection_area((-1,))

    @pyqtSlot(list)
    def handle_channel_concatination(self, concat_list):
        self.fig.clf()
        self.hist_fig.clf()
        if len(concat_list):
            multi_channel = MultiChannels()
            remove_ch = []
            for channel in self.channels:
                exist_count = concat_list.count(str(channel.id))
                if exist_count > 0:
                    multi_channel.add_channel(channel)
                    remove_ch.append(channel)
            self.channels.insert(0, multi_channel)
            
            [self.channels.remove(ch) for ch in remove_ch]
            axs = self.fig.subplots(len(self.channels), 1, sharex='all')
            hist_axs = self.hist_fig.subplots(len(self.channels), 1)
            ch_counter = 0
            for item in self.channels:
                item.axis = axs[ch_counter]
                item.canvas = self.canvas
                item.hist_axis = hist_axs[ch_counter]
                item.hist_canvas = self.hist_canvas
                item.setup_style()
                ch_counter += 1
            self.channelsSettedUp.emit()
        else:
            self.channels.clear()
            self.setup_channels(self.data_header)

        self.canvas.draw()
        self.hist_canvas.draw()

        self.selectDataRequested.emit((-1,))

    @pyqtSlot(dict)
    def feed_progressbar(self, status):
        for key, val in status.items():
            if key == ProgressType.reader:
                self.progress.readingProgressBar.setValue(int(val*100))
            elif key == ProgressType.parser:
                self.progress.parsingProgressBar.setValue(int(val*100))
            elif key == ProgressType.visualizer:
                self.progress.visualizingProgressBar.setValue(int(val*100))
        read_stat = self.progress.readingProgressBar.value()
        parse_stat = self.progress.parsingProgressBar.value()
        visualize_stat = self.progress.visualizingProgressBar.value()
        
        if read_stat == 100 and parse_stat == 100 and visualize_stat == 100:
            self.progress.close()

    def on_filePathChanged(self, file_path):
        if self.default_view:
            self.plotLayout.removeWidget(self.default_view)
            self.default_view.deleteLater()
            self.default_view = None
            self.reviewLayout.addWidget(self.reviewWidget)
            self.plotLayout.addWidget(self.subPlotsWidget)
        self.filePathChanged.emit(file_path)

    def reset_zoom(self):
        for ch in self.channels:
            ch.rescale()

    def on_clearRequested(self):
        self.number_of_fed_channels = 0
        self.progress.readingProgressBar.setValue(0)
        self.progress.parsingProgressBar.setValue(0)
        self.progress.visualizingProgressBar.setValue(0)
        self.clearRequested.emit()

    def export_process(self):
        if self.area_selected():
            self.export_window.show()

    def area_selected(self):
        return self.subPlotsWidget.has_selected_area()

    def on_deleteSelectedReq(self):
        self.feedMood = FeedMood.main_data
        self.deleteSelectedRequested.emit(self.subPlotsWidget.selection_area)
