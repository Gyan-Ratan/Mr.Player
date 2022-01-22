# Universal imports
import os
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

# Local imports
from MrPlayerAbstract import MediaPlayer

class MainWindow(QMainWindow, MediaPlayer):
    """Setup PyMediaPlayer UI, controls and functionalities"""
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        try:
            self.show()                     # show the MainWindow as active
        except Exception as err:
            print("Error in MainWindow:", err)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()                           # Main window of the app
    app.setApplicationName("Mr. Player")            # give name of the application
    sys.exit(app.exec_())                               # Run the app

        # MainWindow is Shown from within the MainWindow class declaration

if __name__ == "__main__":
    main()
