
from PyQt5 import QtCore, QtGui, QtWidgets
from genui import Ui_generate

import cv2
import numpy as np
from pyzbar.pyzbar import decode


class Ui_MainWindow(object):
    #mking other window function to connect
    def connectwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui= Ui_generate()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 109)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0);\n""border-radius:20px")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 93, 28))
        self.pushButton.setStyleSheet("background-color:rgb(0, 191, 0);\n""color:white;\n""border-radius:10px")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 40, 93, 28))
        self.pushButton_2.setStyleSheet("background-color:rgb(0, 191, 0);\n""color:white;\n""border-radius:10px")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 40, 93, 28))
        self.pushButton_3.setStyleSheet("background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")

        #label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 40, 191, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color:rgb(253, 91, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QRWindow"))
        self.pushButton.setText(_translate("MainWindow", "SCAN"))
        self.pushButton_2.setText(_translate("MainWindow", "CREATE"))
        self.pushButton_3.setText(_translate("MainWindow", "ENTRY"))
        self.label.setText(_translate("MainWindow", "status"))

        #connecting buttons to the other window
        self.pushButton_2.clicked.connect(self.connectwindow)
        self.pushButton.clicked.connect(self.checkid)

        #functions

    def checkid(self):
        cap = cv2.VideoCapture(0)
        with open('myDataFile.text') as f:
            myDataList = f.read().splitlines()
        while True:
            success, img = cap.read()
            for barcode in decode(img):
                myData = barcode.data.decode('utf-8')
                print(myData)

                if myData in myDataList:
                    myOutput = 'Authorized'
                    myColor = (0, 255, 0)
                    self.label.setText("Authorized")
                else:
                    myOutput = 'Un-Authorized'
                    myColor = (0, 0, 255)
                    self.label.setText("Un-Authorized")

                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, myColor, 5)
                pts2 = barcode.rect
                cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)

            cv2.imshow('Result', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
