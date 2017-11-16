from PyQt5 import QtWidgets as qt
import sys
from PIL import Image, ImageTk


app = qt.QApplication(sys.argv)
root = qt.QWidget()
root.setWindowTitle('G - algorithm')
root.showMaximized()
sys.exit(app.exec_())
