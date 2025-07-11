#!/usr/bin/env python3
import sys
import os
# Set the QT_QPA_PLATFORM environment variable to use the offscreen platform
os.environ["QT_QPA_PLATFORM"] = "offscreen"
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class HelloWorldApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Set window title and size
        self.setWindowTitle('Hello World PyQt App')
        self.resize(400, 200)
        
        # Create a vertical layout
        layout = QVBoxLayout()
        
        # Create a label with "Hello World" text
        hello_label = QLabel('Hello World!', self)
        hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hello_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        
        # Create a button that will print "Hello World" to console when clicked
        print_button = QPushButton('Print Hello World', self)
        print_button.clicked.connect(self.print_hello)
        
        # Add widgets to layout
        layout.addWidget(hello_label)
        layout.addWidget(print_button)
        
        # Set the layout for the window
        self.setLayout(layout)
        
        # Center the window on the screen
        self.center()
        
    def center(self):
        # Get the geometry of the window
        qr = self.frameGeometry()
        # Get the center point of the screen
        cp = self.screen().availableGeometry().center()
        # Move the window's center point to the screen's center point
        qr.moveCenter(cp)
        # Move the top-left point of the window to the top-left point of qr
        self.move(qr.topLeft())
        
    def print_hello(self):
        print("Hello World!")

if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the window
    window = HelloWorldApp()
    window.show()
    # Run the application
    sys.exit(app.exec_())