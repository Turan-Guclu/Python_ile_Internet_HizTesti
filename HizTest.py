# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import speedtest
import matplotlib.pyplot  as plt
import numpy as np

class Ui_Dialog(object):

    def setupUi(self, Dialog):
            

        Dialog.setObjectName("Dialog")
        Dialog.resize(485, 446)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.HzBasla = QtWidgets.QPushButton(Dialog)
        self.HzBasla.setGeometry(QtCore.QRect(170, 70, 121, 81))
        self.HzBasla.setObjectName("HzBasla")
        self.grafik = QtWidgets.QPushButton(Dialog)
        self.grafik.setGeometry(QtCore.QRect(170, 400, 141, 23))
        self.grafik.setObjectName("grafik")
        self.yazi = QtWidgets.QTextEdit(Dialog)
        self.yazi.setGeometry(QtCore.QRect(30, 170, 411, 201))
        self.yazi.setObjectName("yazi")
    
        self.retranslateUi(Dialog)
        self.HzBasla.clicked.connect(self.testbaslat)
        self.grafik.clicked.connect(self.hata_yakala)
        self.HzBasla.clicked.connect(Dialog.repaint)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Turan Güçlü Hız Testi"))
        Dialog.setWindowIcon(QIcon('hiztest.png'))
        self.label.setText(_translate("Dialog", "Turan Güçlü Hız Testi"))
        self.HzBasla.setText(_translate("Dialog", "BAŞLA"))
        self.grafik.setText(_translate("Dialog", "Grafik Olarak Önizle"))

    def hata_yakala(self):
        try:
            self.grafikciz()
        except AttributeError:
            self.yazi.setText("Grafiği Çizmeden Önce Testi Başlatmalısınız!...")
       

    def testbaslat(self):
        self.downl=[]
        self.upl=[]     
        self.test = speedtest.Speedtest()
        self.down = self.test.download()
        self.up = self.test.upload()
        self.down_speed=round(self.down/(10**6),2)
        self.up_speed=round(self.up/(10**6),2)
        self.downl.append(self.down_speed)
        self.upl.append(self.up_speed)
        downsonuc=f"Download Hızınız: {self.down_speed} Mbps"
        upsonuc=f"Upload Hızınız: {self.up_speed} Mbps"
        self.yazi.append(f"{downsonuc}\n{upsonuc}\n")

    def grafikciz(self):
        labels=["Yüksek Değer İyidir"]
        x=np.arange(len(labels))      
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, self.downl, width, label='Downloads')
        rects2 = ax.bar(x + width/2, self.upl, width, label='Uploads')
        ax.set_ylabel('Değer Aralığı(Mbps)')
        ax.set_title('Hız Testi Sonucunuz')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        def autolabel(rects):
        # Attach a text label above each bar in *rects*, displaying its height
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
        
        autolabel(rects1)
        autolabel(rects2)
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
