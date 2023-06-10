import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLineEdit, QCheckBox, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from normalization import normalize_audio
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGridLayout, QLabel, QSpacerItem, QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WAV File Processing")

        # Create a central widget and set its layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create a layout for the top row
        self.top_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        spacer = QSpacerItem(self.width(), 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Create a text field for entering a number
        self.normalization_field = QLineEdit(self)
        self.normalization_field.setPlaceholderText("Normalization gain")
        self.top_layout.addWidget(self.normalization_field)

        # Create a checkbox for enabling normalization
        self.normalization_checkbox = QCheckBox("Enable Normalization", self)
        self.top_layout.addWidget(self.normalization_checkbox)

        self.top_layout.addSpacerItem(spacer)

        # Create a layout for the bottom row
        self.bottom_layout = QGridLayout()
        self.main_layout.addLayout(self.bottom_layout)

        # Create a button to select the directory
        self.select_button = QPushButton("Select Directory", self)
        self.select_button.clicked.connect(self.select_directory)

        # Set the size policy of the button to expand vertically
        self.select_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add the button to the bottom layout
        self.bottom_layout.addWidget(self.select_button, 0, 0, 1, 2)


    def select_directory(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Select Directory", options=options)
        if directory:
            normalization_gain = self.normalization_field.text()
            enable_normalization = self.normalization_checkbox.isChecked()
            self.process_wav_files(directory, normalization_gain, enable_normalization)

    def process_wav_files(self, directory, normalization_gain, enable_normalization):
        for filename in os.listdir(directory):
            if filename.endswith('.wav'):
                file_path = os.path.join(directory, filename)
                self.process_wav_file(file_path, normalization_gain, enable_normalization)

    def process_wav_file(self, file_path, normalization_gain, enable_normalization):
        # Apply your processing logic to the WAV file, using the provided number
        print("Processing:", file_path)
        if enable_normalization:
            normalize_audio(file_path, normalization_gain)

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = MainWindow()
window.show()  # Maximize the window to full screen

# Start the event loop
sys.exit(app.exec_())


