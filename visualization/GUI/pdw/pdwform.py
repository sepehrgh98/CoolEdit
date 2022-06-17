import os
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from visualization.Radar.radarcontroller import RadarController
from visualization.pdw.Channel.channel import Channel
from visualization.GUI.pdw.pdwinformationbox import PDWInformationBoxForm
from visualization.GUI.pdw.pdwtools import PDWToolsForm
from visualization.GUI.pdw.datainformationform import DataInformationForm
from visualization.visualizationparams import DataPacket
from matplotlib.figure import Figure
from visualization.GUI.pdw.subplotwidget import SubPlotWidget
from visualization.GUI.radar.radarform import RadarForm
import numpy as np

Form = uic.loadUiType(os.path.join(os.getcwd(), 'visualization', 'GUI', 'pdw', 'pdwui.ui'))[0]


#
# def find_nearest_value_indx(array, value):
#     array = np.asarray(array)
#     idx = (np.abs(array - value)).argmin()
#     return idx


class PDWForm(QMainWindow, Form):
    filePathChanged = pyqtSignal(str)
    totalDataSizeChanged = pyqtSignal(int)
    dataRequested = pyqtSignal(tuple, tuple)  # time range & value range
    selectedDataIsReady = pyqtSignal(DataPacket)

    def __init__(self):
        super(PDWForm, self).__init__()
        self.setupUi(self)

        # setup figure
        self.fig = Figure()

        # widgets
        self.infBoxWidget = PDWInformationBoxForm()
        self.toolsWidget = PDWToolsForm()
        self.dataInfoWidget = DataInformationForm()
        self.rightFrameLayout.addWidget(self.toolsWidget)
        self.rightFrameLayout.addWidget(self.infBoxWidget)
        self.dataInformationLayout.addWidget(self.dataInfoWidget)
        self.subPlotsWidget = SubPlotWidget(self.fig)
        self.leftVerticalLayout.addWidget(self.subPlotsWidget)
        self.radar_form = RadarForm()
        # self.radar_controller = RadarController()

        self.navtool = self.subPlotsWidget.get_nav_tool()
        self.rightFrameLayout.addWidget(self.navtool)

        # variables
        self.canvas = self.subPlotsWidget.get_canvas()
        self.channels = []
        self.selection_area_x = (-1, -1)
        self.selection_area_y = (-1, -1)
        self.selection_area_updated = False
        self.selection_area_indx = (-1, -1)

        # initialization
        self.setup_connections()

    def setup_connections(self):
        self.toolsWidget.filePathChanged.connect(self.filePathChanged)
        self.toolsWidget.filePathChanged.connect(self.dataInfoWidget.set_file_name)
        # self.toolsWidget.dataRequested.connect(self.dataRequested)
        self.totalDataSizeChanged.connect(self.dataInfoWidget.set_total_data_size)
        self.toolsWidget.selectBtnPressed.connect(self.subPlotsWidget.enable_select_action)
        self.subPlotsWidget.selectionRangeHasBeenSet.connect(self.set_selection_area)
        self.toolsWidget.radarRequested.connect(self.initialize_new_radar)
        self.selectedDataIsReady.connect(self.radar_form.feed)

    @pyqtSlot(dict)
    def setup_channels(self, header):
        self.radar_form.setup_channel(header)
        axs = self.fig.subplots(len(header.items()), 1, sharex='all')
        ch_counter = 0
        for _id, _name in header.items():
            ch = Channel(_id, _name, axs[ch_counter], self.canvas)
            ch.setup_style()
            self.channels.append(ch)
            ch_counter += 1
        self.canvas.draw()

    @pyqtSlot(DataPacket)
    def feed(self, data_packet):
        for channel in self.channels:
            if channel.id == data_packet.id:
                if self.selection_area_x == (-1, -1) or self.selection_area_y == (-1, -1):
                    channel.feed(data_packet.key, data_packet.data, "#ADD8E6", mood="initilize")
                else:
                    channel.feed(data_packet.key, data_packet.data, "red", mood="selection")
                    self.selectedDataIsReady.emit(data_packet)

        self.canvas.draw()
        self.canvas.flush_events()

    @pyqtSlot(tuple, tuple)
    def set_selection_area(self, x_range, y_range):
        self.selection_area_x = x_range
        self.selection_area_y = y_range
        self.selection_area_updated = True
        self.dataRequested.emit(self.selection_area_x, self.selection_area_y)

    @pyqtSlot()
    def initialize_new_radar(self):
        self.radar_form.show()
