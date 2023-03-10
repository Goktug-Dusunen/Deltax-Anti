import os
import hashlib
import numpy as np
import urllib.request
from sklearn.svm import SVC
import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
import sys

class AntiVirus(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.databases = [("https://virusshare.com/hashfiles/VirusShare_00000.md5", "VirusShare_00000.md5"),
                          ("https://virusshare.com/hashfiles/VirusShare_00001.md5", "VirusShare_00001.md5"),
                          ("https://virusshare.com/hashfiles/VirusShare_00002.md5", "VirusShare_00002.md5"),
                         ]
        self.features = []
        self.labels = []
        self.model = SVC(kernel='linear')

    def initUI(self):
        self.setWindowTitle("DeltaX-Anti")
        self.setWindowIcon(QtGui.QIcon("deltax-icon.png"))
        self.setGeometry(100, 100, 600, 500)
        self.create_widgets()
        self.show()

    def create_widgets(self):
        self.start_scan_btn = QtWidgets.QPushButton("Start Scan", self)
        self.start_scan_btn.move(200, 400)
        self.start_scan_btn.clicked.connect(self.start_scan)

        self.stop_scan_btn = QtWidgets.QPushButton("Stop Scan", self)
        self.stop_scan_btn.move(300, 400)
        self.stop_scan_btn.clicked.connect(self.stop_scan)

        self.select_directory_btn = QtWidgets.QPushButton("Select Directory", self)
        self.select_directory_btn.move(100, 400)
        self.select_directory_btn.clicked.connect(self.select_directory)

        self.update_db_btn = QtWidgets.QPushButton("Update Database", self)
        self.update_db_btn.move(400, 400)
        self.update_db_btn.clicked.connect(self.update_database)

        self.scan_results_label = QtWidgets.QLabel(self)
        self.scan_results_label.setText("Scan Results:")
        self.scan_results_label.move(50, 50)

        self.results_display = QtWidgets.QTextEdit(self)
        self.results_display.setReadOnly(True)
        self.results_display.move(50, 80)

    def update_database(self):
        self.features = []
        self.labels = []
        self.results_display.setText("")
        for url, file_name in self.databases:
            urllib.request.urlretrieve(url, file_name)
        self.results_display.append("Database updated successfully.")
def start_scan(self):
    try:
        self.scan_status_label.setText("Scanning...")
        if self.directory_path:
            self.scan_directory(self.directory_path)
            if not np.any(self.labels == -1):
                self.train_model(self.features, self.labels)
                for file in self.infected_files:
                    os.remove(file)
                    self.results_display.append(f"Removed {file} as it was infected.")
                self.scan_status_label.setText("Scan Completed")
                QMessageBox.information(self, "Scan Results", "Scan Completed Successfully. No virus was found.")
            else:
                self.results_display.setText("No virus was found.")
                self.scan_status_label.setText("Scan Completed")
                QMessageBox.information(self, "Scan Results", "Scan Completed Successfully. No virus was found.")
    except Exception as e:
        # Handle the exception here
        self.results_display.append(f"An error occurred during the scan: {e}")
        self.scan_status_label.setText("Scan Failed")
