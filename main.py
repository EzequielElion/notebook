from PyQt5 import uic,QtWidgets
from PyQt5 import uic,  QtCore, QtGui, QtWidgets
import time , sys, os
from PyQt5.QtWidgets import *
import datetime

 

def Main():
    MainPage.show()

def New():
    NewPage.show()
def closeMainPage():
    sys.exit()

def closeNewPage():

    valor = NewPage.lineEdit.text()
    descricao = NewPage.lineEdit_2.text()
    hora = datetime.datetime.now()
    fiado = ""
    cliente =""
    if NewPage.radioButton.isChecked() :
        fiado = "nao pago"
        cliente = ClientPage.lineEdit_2.text()
    else :
        fiado = "Pago"
    print(valor, descricao,hora,fiado)
    

def mostrar():
    
    ClientPage.destroy()
    NewPage.destroy()


     
    


def mousePressEvent(MainPage, event):
    MainPage.dragPos = event.globalPosition().toPoint()


def mouseMoveEvent(MainPage, event):
    MainPage.move(MainPage.pos() + event.globalPosition().toPoint() - MainPage.dragPos )
    MainPage.dragPos = event.globalPosition().toPoint()
    event.accept()


app=QtWidgets.QApplication([])
MainPage = uic.loadUi("MainPageNotebook.ui")
MainPage.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
MainPage.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
NewPage=uic.loadUi("new.ui")
NewPage.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
NewPage.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
NewPage.pushButton_3.clicked.connect(closeNewPage)
NewPage.pushButton.clicked.connect(closeNewPage)
MainPage.pushButton.clicked.connect(New)
MainPage.pushButton_3.clicked.connect(closeMainPage)
ClientPage=uic.loadUi("cliente.ui")
ClientPage.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
ClientPage.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
ClientPage.pushButton.clicked.connect(mostrar)
Main()

app.exec()