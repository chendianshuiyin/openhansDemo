#!/usr/bin/env python3
import sys
import os
# Set the QT_QPA_PLATFORM environment variable to use the offscreen platform
os.environ["QT_QPA_PLATFORM"] = "offscreen"
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

def print_hello_world():
    print("Hello World!")
    # Exit the application after printing
    app.quit()

if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)
    
    # Use a timer to print "Hello World" after 100ms
    QTimer.singleShot(100, print_hello_world)
    
    # Run the application
    sys.exit(app.exec_())