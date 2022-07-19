from tkinter.messagebox import NO
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot, QThread
from numpy import double

class SReader(QObject):
    batch_is_ready = pyqtSignal(list, bool, float)
    progress_is_ready = pyqtSignal(float)
    def __init__(self, batch_size=10000) :
        super(SReader, self).__init__()
        self.batch_size = batch_size
        self.file_path = None
        self.progress = 0

        # moving to thread
        self.objThread = QThread()
        self.moveToThread(self.objThread)
        self.objThread.finished.connect(self.objThread.deleteLater)
        self.objThread.start()

    
    @pyqtSlot(str)
    def set_file_path(self, file_path) :
        if file_path != self.file_path:
            self.file_path = file_path
            self.start()

    def start(self):
        file_total_size = 0
        with open(self.file_path, "r") as f:
            file_total_size = len(f.readlines())

        with open(self.file_path, "r") as f:
            self.progress = 0
            result = []
            for line in f:
                result.append(line)
                if len(result) == self.batch_size:
                    self.progress = self.progress + (self.batch_size/file_total_size)
                    self.progress_is_ready.emit(self.progress)
                    self.batch_is_ready.emit(result, False, file_total_size)
                    result.clear()
            self.progress = self.progress + (self.batch_size/file_total_size)
            self.progress_is_ready.emit(self.progress)
            self.batch_is_ready.emit(result, True, file_total_size)

                    
                    
