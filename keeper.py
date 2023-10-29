from PySide2.QtWidgets import *
from keeper_ui import Ui_SSK
import sys
import getpass
import saver

__author__ = 'ferret22'


class KeeperWin(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_SSK()
        self.ui.setupUi(self)

        self.error = QErrorMessage(self)
        self.message = QMessageBox(self)

        self.user_name = getpass.getuser()
        self.saves_path = r'C:\Users\%s\Documents\My Games\Skyrim\Saves' % self.user_name
        self.save_path = r'C:\Users\%s\Documents\SSK' % self.user_name
        saver.create_folder(self.save_path)

        self.ui.ButtonSave.clicked.connect(self.save_skyrim_saves)

    def save_skyrim_saves(self):
        self.ms_message('Saving...', 'Saved', QMessageBox.Information)
        saver.copy_saves(self.saves_path, self.save_path)

    def ms_error(self, title: str, message: str, type_error: str):
        self.error.setWindowTitle(title)
        self.error.showMessage(message, type_error)

    def ms_message(self, title: str, message: str, icon):
        self.message.setWindowTitle(title)
        self.message.setIcon(icon)
        self.message.setText(message)
        self.message.show()


def start_keeper():
    app = QApplication(sys.argv)
    keeper = KeeperWin()
    keeper.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_keeper()
