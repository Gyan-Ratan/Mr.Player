# Instructions:-
# 1. Install libraries:- pyqt5, pyqt5-tools, stagger, pillow
# 2. Icons folder should be correctly placed


# Universal imports
import os
import sys
import tempfile
import shutil
from PyQt5.QtWidgets import QMainWindow

# Local imports
from MrPlayerAbstract import MediaPlayer, hostOS
from SingleApplication import SingleApplicationWithMessaging, SingleApplication


class MainWindow(QMainWindow, MediaPlayer):
    """Setup PyMediaPlayer UI, controls and functionalities"""
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        try:
            self.show()                     # show the MainWindow as active
        except Exception as err:
            print("Error in MainWindow:", err)


def main():
    # Unique key of the app (Shouldn't match with other apps in the Host system !!!!!)
    key = 'PYMEDIAPLAYER-PYQT5-CHARITRA-AGARWAL'

    # send commandline args as message
    if len(sys.argv) >= 1:
        app = SingleApplicationWithMessaging(sys.argv, key)
        if app.isRunning():
            print('Sending parameters to already running instance of app and Exiting.')
            app.sendMessage(';'.join(sys.argv))
    else:
        app = SingleApplication(sys.argv, key)
        if app.isRunning():
            print('Another instance of app is already running. Exiting.')

    if not app.isRunning():
        # Run the new instance if the app is not running
        window = MainWindow()                               # Main window of the app
        app.setApplicationName("Mr. Player")            # give name of the application
        sys.exit(app.exec_())                               # Run the app

        # MainWindow is Shown from within the MainWindow class declaration


if __name__ == "__main__":
    main()
