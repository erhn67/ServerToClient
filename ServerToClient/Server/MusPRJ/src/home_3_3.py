from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sys, os
from PyQt5.QtCore import Qt, QUrl
import pygame,time
from home_3_python import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QFileDialog,QWidget,QMessageBox



class HomePage(QMainWindow):

	def __init__(self):
		super().__init__()
		
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)

	def getPath(self):
		path,_= QFileDialog.getOpenFileName(self,"Anons Yükle",os.getenv("HOME"),"Dosyası Uzantısı(*.mp3)")
		return path
	
	def show_massage(self,title,text):

		message_box=QMessageBox(self) #ana window ikonu verir.
		message_box.setIcon(QMessageBox.Warning)
		#message_box.setWindowIcon(QIcon(":/icons/icons/warning.jpg"))
		message_box.setWindowTitle(title)
		message_box.setText(text)
		message_box.setStandardButtons(QMessageBox.Ok)
		button_ok=message_box.button(QMessageBox.Ok)
		button_ok.setText("Tamam")

		message_box.exec_()




