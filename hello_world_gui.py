#!/usr/bin/env python3
"""
A simple PyQt5 application that displays a window with "Hello World" text
and a button that prints "Hello World" to the console when clicked.
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, 
    QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class HelloWorldWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # Set window properties
        self.setWindowTitle('Hello World PyQt Application')
        self.setGeometry(100, 100, 400, 200)  # x, y, width, height
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        
        # Create a label with "Hello World" text
        hello_label = QLabel('Hello World!')
        hello_label.setAlignment(Qt.AlignCenter)
        hello_label.setFont(QFont('Arial', 24, QFont.Bold))
        
        # Create buttons layout
        buttons_layout = QHBoxLayout()
        
        # Create a button that prints "Hello World" to console
        print_button = QPushButton('Print to Console')
        print_button.clicked.connect(self.print_hello)
        
        # Create a button to quit the application
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(self.close)
        
        # Add buttons to the layout
        buttons_layout.addWidget(print_button)
        buttons_layout.addWidget(quit_button)
        
        # Add widgets to main layout
        main_layout.addWidget(hello_label)
        main_layout.addLayout(buttons_layout)
        
    def print_hello(self):
        print("Hello World!")

def main():
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()