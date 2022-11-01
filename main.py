# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import qrcode
from qr0 import *
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PIL.ImageQt import ImageQt

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
  
def olustur():
    bilgi=ui.lineEdit.text()
    img= qrcode.make(bilgi)

    qimage = ImageQt(img)
    pixmap= QtGui.QPixmap.fromImage(qimage)
    
    ui.label_3.setPixmap(QtGui.QPixmap(pixmap))
    


def kaydet():
    bilgi=ui.lineEdit.text()
    img= qrcode.make(bilgi)
    img.save("saved/"+ bilgi+".jpg")

ui.pushButton_2.clicked.connect(olustur)    
ui.pushButton.clicked.connect(kaydet)
sys.exit(app.exec_())



