import sys
import qrcode
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


class Ui_generate(object):
    def setupUi(self, generate):
        generate.setObjectName("generate")
        generate.resize(555, 340)
        generate.setStyleSheet("background-color:rgb(0, 0, 0);\n""border-radius:20px")
        self.centralwidget = QtWidgets.QWidget(generate)
        self.centralwidget.setObjectName("centralwidget")

        #display label
        self.label = QtWidgets.QLabel(generate)
        self.label.setText("Make QRcode Here")
        self.label.move(380, 350)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color:rgb(253, 91, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.label.setGeometry(QtCore.QRect(310, 255, 200, 50))  # start end width

        #display photo
        self.code = QtWidgets.QLabel(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(280, 20, 251, 221))
        self.code.setText("")
        self.code.setPixmap(QtGui.QPixmap("barcodedata/qrcode1.png"))
        self.code.setScaledContents(True)
        self.code.setObjectName("code")

        self.pushcreate = QtWidgets.QPushButton(self.centralwidget)
        self.pushcreate.setGeometry(QtCore.QRect(70, 100, 121, 41))
        self.pushcreate.setStyleSheet("background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.pushcreate.setObjectName("pushcreate")

        self.pushsave = QtWidgets.QPushButton(self.centralwidget)
        self.pushsave.setGeometry(QtCore.QRect(70, 170, 121, 41))
        self.pushsave.setStyleSheet("background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.pushsave.setObjectName("pushsave")

        self.pushexit = QtWidgets.QPushButton(self.centralwidget)
        self.pushexit.setGeometry(QtCore.QRect(70, 240, 121, 41))
        self.pushexit.setStyleSheet("background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.pushexit.setObjectName("pushexit")

        #text input
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 50, 241, 31))
        self.name.setStyleSheet("background-color:rgb(85, 255, 255);\n""color:rgb(0, 0, 0);\n""border-radius:10px")
        self.name.setObjectName("name")
        print(self.name)

        generate.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(generate)
        self.statusbar.setObjectName("statusbar")
        generate.setStatusBar(self.statusbar)

        self.retranslateUi(generate)
        QtCore.QMetaObject.connectSlotsByName(generate)

    def retranslateUi(self, generate):
        _translate = QtCore.QCoreApplication.translate
        generate.setWindowTitle(_translate("generate", "QR Generator"))
        self.pushcreate.setText(_translate("generate", "CREATE"))
        self.pushsave.setText(_translate("generate", "SAVE"))
        self.pushexit.setText(_translate("generate", "EXIT"))

    #connecting buttons to functions
        self.pushcreate.clicked.connect(self.qrmaker)
        self.pushsave.clicked.connect(self.saveqr)
        self.pushexit.clicked.connect(self.exit)

    #FUNCTIONS

    def info(self):
        text=self.name.text()
        return text

    #making qrcode
    def qrmaker(self):
        x=1
        self.label.setText("creatig QRcode")
        img = qrcode.make(self.info())
        print(type(img))
        print(img.size)
        print(self.name)
        img.save('barcodedata/qrcode{no}.png'.format(no=(x)))


    #appending into file and saving qrcode
    def saveqr(self):
        self.label.setText("saving QRcode")
        file = open("myDataFile.text", "a+")
        try:
            file.write(self.info())
            file.write("\n")
        finally:
            file.close()

    #exit the window
    def exit(self):
        self.label.setText("exit the window")
        sys.exit(app.exec_())

    def update(self):
        self.label.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    generate = QtWidgets.QMainWindow()
    ui = Ui_generate()
    ui.setupUi(generate)
    generate.show()
    sys.exit(app.exec_())
