from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sys, os
from PyQt5.QtCore import Qt, QUrl
import pygame,time
from ui.home_3_python import Ui_MainWindow



class HomePage(QMainWindow):

	def __init__(self):
		super().__init__()
		pygame.init()

		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)

		self.dosyaSecildi = False
		self.dosyaPath = ""

		self.twiceclick=False
		self.twice_play_pause=False
		self.clicked_list_twice=False
		self.playsound=None
		self.pause=None
		self.MUSIC_END=0
		

		self.ui.pushButton_hoparlor_1.setCheckable(True)
		self.ui.pushButton_hoparlor_2.setCheckable(True)
		self.ui.pushButton_hoparlor_3.setCheckable(True)
		self.ui.pushButton_hoparlor_4.setCheckable(True)
		self.ui.pushButton_hoparlor_5.setCheckable(True)
		self.ui.pushButton_hoparlor_6.setCheckable(True)
		self.ui.pushButton_hoparlor_7.setCheckable(True)
		self.ui.pushButton_hoparlor_8.setCheckable(True)
		

		self.ui.pushButton_hoparlor_1.clicked.connect(self.hoparlor_1_clicked)
		self.ui.pushButton_hoparlor_2.clicked.connect(self.hoparlor_2_clicked)
		self.ui.pushButton_hoparlor_3.clicked.connect(self.hoparlor_3_clicked)
		self.ui.pushButton_hoparlor_4.clicked.connect(self.hoparlor_4_clicked)
		self.ui.pushButton_hoparlor_5.clicked.connect(self.hoparlor_5_clicked)
		self.ui.pushButton_hoparlor_6.clicked.connect(self.hoparlor_6_clicked)
		self.ui.pushButton_hoparlor_7.clicked.connect(self.hoparlor_7_clicked)
		self.ui.pushButton_hoparlor_8.clicked.connect(self.hoparlor_8_clicked)

		self.radioGroup = QButtonGroup()
		self.ui.radioButton_anons1.toggled.connect(self.anons1_radobutton)
		self.ui.radioButton_anons2.toggled.connect(self.anons2_radobutton)
		self.ui.radioButton_anons3.toggled.connect(self.anons3_radobutton)
		self.radioGroup.addButton(self.ui.radioButton_anons1)
		self.radioGroup.addButton(self.ui.radioButton_anons2)
		self.radioGroup.addButton(self.ui.radioButton_anons3)
		
			

		self.clicked_list=[]



		self.ui.pushButton_ses_gonder.clicked.connect(self.yazdir_clicked)

		self.ui.pushButton_usbden_yukle.clicked.connect(self.usbden_yukle)

		self.ui.stopButton.setEnabled(False)
		self.ui.playButton.setEnabled(False)
		

		self.ui.playButton.clicked.connect(self.play_the_songs)
		self.ui.stopButton.clicked.connect(self.stop_the_songs)

	
			
#=============================================================================================


	def  hoparlor_1_clicked(self):

		if self.ui.pushButton_hoparlor_1.isChecked()==1:

			self.ui.pushButton_hoparlor_1.setStyleSheet("border-image: url(:/icons/icons/koyu_yesil.jpg);")
			self.clicked_list.append("Anons Hoparlör 1'e gönderildi.")
			self.ui.label_hoparlor_1.setStyleSheet("color:green")
			print("Hoparlör 1 aktif edildi")
			#self.twiceclick=False
					
			
			
		else:
			self.ui.pushButton_hoparlor_1.setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
			self.clicked_list.remove("Anons Hoparlör 1'e gönderildi.")
			print("Hoparlör 1 pasif edildi")
			self.ui.label_hoparlor_1.setStyleSheet("color: rgb(170, 0, 0);")

#=============================================================================================

	def hoparlor_2_clicked(self):

		if self.ui.pushButton_hoparlor_2.isChecked()==1:

			self.ui.pushButton_hoparlor_2.setStyleSheet("border-image: url(:/icons/icons/koyu_yesil.jpg);")
			self.clicked_list.append("Anons Hoparlör 2'ye gönderildi.")
			self.ui.label_hoparlor_2.setStyleSheet("color:green")
			print("Hoparlör 2 aktif edildi")
			#self.clicked_list_twice=False
		#

		else:
			self.ui.pushButton_hoparlor_2.setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
			self.ui.label_hoparlor_2.setStyleSheet("color: rgb(170, 0, 0);")
			self.clicked_list.remove("Anons Hoparlör 2'ye gönderildi.")
			print("Hoparlör 2 pasif edildi")
#=============================================================================================

	def hoparlor_3_clicked(self):

		if self.ui.pushButton_hoparlor_3.isChecked()==1:

			self.ui.pushButton_hoparlor_3.setStyleSheet("border-image: url(:/icons/icons/koyu_yesil.jpg);")
			self.clicked_list.append("Anons Hoparlör 3'e gönderildi.")
			self.ui.label_hoparlor_3.setStyleSheet("color:green")
			print("Hoparlör 3 aktif edildi")
		#

		else:
			self.ui.pushButton_hoparlor_3.setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
			self.ui.label_hoparlor_3.setStyleSheet("color: rgb(170, 0, 0);")
			self.clicked_list.remove("Anons Hoparlör 3'e gönderildi.")
			print("Hoparlör 3 pasif edildi")
#=============================================================================================

	def hoparlor_4_clicked(self):

		if self.ui.pushButton_hoparlor_4.isChecked()==1:

			self.ui.pushButton_hoparlor_4.setStyleSheet("border-image: url(:/icons/icons/koyu_yesil.jpg);")
			self.clicked_list.append("Anons Hoparlör 4'e gönderildi.")
			self.ui.label_hoparlor_4.setStyleSheet("color:green")
			print("Hoparlör 4 aktif edildi")
		#

		else:
			self.ui.pushButton_hoparlor_4.setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
			self.ui.label_hoparlor_4.setStyleSheet("color: rgb(170, 0, 0);")
			self.clicked_list.remove("Anons Hoparlör 4'e gönderildi.")
			print("Hoparlör 4 pasif edildi")
#=============================================================================================

	def hoparlor_5_clicked(self):

		if self.ui.pushButton_hoparlor_5.isChecked()==1:
			self.ui.pushButton_hoparlor_5.setStyleSheet("border-image: url(:/icons/icons/koyu_yesil.jpg);")
			self.clicked_list.append("Anons Hoparlör 5'e gönderildi.")
			self.ui.label_hoparlor_5.setStyleSheet("color:green")
			print("Hoparlör 5 aktif edildi")
		#

		else:
			self.ui.pushButton_hoparlor_5.setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
			self.ui.label_hoparlor_5.setStyleSheet("color: rgb(170, 0, 0);")
			self.clicked_list.remove("Anons Hoparlör 5'e gönderildi.")
			print("Hoparlör 5 pasif edildi")
#=============================================================================================
	def hoparlor_6_clicked(self):

		if self.ui.pushButton_hoparlor_6.isChecked()==1:
			self.ui.pushButton_hoparlor_6.setStyleSheet("border-image: url(:/icons/icons/koyu_yesil.jpg);")
			self.clicked_list.append("Anons Hoparlör 6'ya gönderildi.")
			self.ui.label_hoparlor_6.setStyleSheet("color:green")
			print("Hoparlör 6 aktif edildi")
		#

		else:
			self.ui.pushButton_hoparlor_6.setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
			self.clicked_list.remove("Anons Hoparlör 6'ya gönderildi.")
			self.ui.label_hoparlor_6.setStyleSheet("color: rgb(170, 0, 0);")
			print("Hoparlör 6 pasif edildi")
#=============================================================================================
	def hoparlor_7_clicked(self):

		if self.ui.pushButton_hoparlor_7.isChecked()==1:
			self.ui.pushButton_hoparlor_7.setStyleSheet("border-image: url(:/icons/icons/koyu_yesil.jpg);")
			self.clicked_list.append("Anons Hoparlör 7'ye gönderildi.")
			self.ui.label_hoparlor_7.setStyleSheet("color:green")
			print("Hoparlör 7 aktif edildi")
		#

		else:
			self.ui.pushButton_hoparlor_7.setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
			self.clicked_list.remove("Anons Hoparlör 7'ye gönderildi.")
			self.ui.label_hoparlor_7.setStyleSheet("color: rgb(170, 0, 0);")
			print("Hoparlör 7 pasif edildi")
#=============================================================================================
	def hoparlor_8_clicked(self):

		if self.ui.pushButton_hoparlor_8.isChecked()==1:
			self.ui.pushButton_hoparlor_8.setStyleSheet("border-image: url(:/icons/icons/koyu_yesil.jpg);")
			self.clicked_list.append("Anons Hoparlör 8'e gönderildi.")
			self.ui.label_hoparlor_8.setStyleSheet("color:green")
			print("Hoparlör 8 aktif edildi")
		#

		else:
			self.ui.pushButton_hoparlor_8.setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
			self.ui.label_hoparlor_8.setStyleSheet("color: rgb(170, 0, 0);")
			self.clicked_list.remove("Anons Hoparlör 8'e gönderildi.")
			print("Hoparlör 8 pasif edildi")
#=============================================================================================
	def yazdir_clicked(self):
		

		if self.twiceclick is not True:
			tikliolan = 0
			if self.ui.radioButton_anons1.isChecked():
				tikliolan=1		
			elif self.ui.radioButton_anons2.isChecked():
				tikliolan=2
			elif self.ui.radioButton_anons3.isChecked():
				tikliolan=3
			elif self.dosyaSecildi:
				self.dosyaPath

			if len(self.clicked_list) == 0 and tikliolan == 0 and self.dosyaPath=="":
				print(self.clicked_list)
				self.show_massage("Hatalı Giriş","Hoparlor ve Anons seçilmedi.")
				return
			elif len(self.clicked_list) == 0:
				self.show_massage("Hatalı Giriş","Hoparlor seçilmedi ")
				return
			
			elif tikliolan == 0 and self.dosyaPath=="":
				self.show_massage("Hatalı Giriş","Anons seçilmedi ")
				return
		
			for h in self.clicked_list:

				if self.dosyaSecildi:
					self.gonder(h,self.dosyaPath)
				elif tikliolan==1:
					self.gonder(h,1)
				elif tikliolan==2:
					self.gonder(h,2)
				elif tikliolan==3:
					self.gonder(h,3)
				
			self.twiceclick=True
			
		else:				
			self.ui.statusbar.showMessage("Aynı Anons 2. kez gönderilemez ",3000)
			self.show_massage("Hatalı Giriş","Aynı Anons 2. kez gönderilemez ")
						
			
#==========================================================================================================		

	def gonder(self,hoparlor,sesdatasi):

		
		print(hoparlor)

		if sesdatasi==1:
			#self.dosyaSecildi = False
			pygame.mixer.init()
			print ("Anons 1 çalıyor")
				
			Track_1= pygame.mixer.music.load ( "C:\\Users\\Erhan67\\Desktop\\PyCharmProjeler\\test_proje\\sound\\anons_1.mp3")
			pygame.mixer.music.play()
			self.ui.playButton.setEnabled(False)
			self.ui.stopButton.setEnabled(True)
				
			
		elif sesdatasi==2:
			#self.dosyaSecildi = False
			pygame.mixer.init()
			print ("Anons 2 çalıyor")
				
			Track_2 = pygame.mixer.music.load ( "C:\\Users\\Erhan67\\Desktop\\PyCharmProjeler\\test_proje\\sound\\anons_2.mp3")
			
			pygame.mixer.music.play()
			self.ui.playButton.setEnabled(False)
			self.ui.stopButton.setEnabled(True)
	
		elif sesdatasi==3:
			#self.dosyaSecildi = False
			pygame.mixer.init()
			print ("Anons 3 çalıyor")
				
			Track_3= pygame.mixer.music.load ( "C:\\Users\\Erhan67\\Desktop\\PyCharmProjeler\\test_proje\\sound\\anons_3.mp3")
				
			pygame.mixer.music.play()
			self.ui.playButton.setEnabled(False)
			self.ui.stopButton.setEnabled(True)

		elif self.dosyaPath:
			pygame.mixer.init()
			pygame.mixer.music.load(self.dosyaPath)
			print(self.dosyaPath+" Çalıyor")
			pygame.mixer.music.play()
			self.ui.playButton.setEnabled(False)
			self.ui.stopButton.setEnabled(True)
			
		

		print(sesdatasi)
		
#=============================================================================================
	
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
	
#=============================================================================================
	def usbden_yukle(self):

		import os
		import ntpath
		self.playsound=None
		path,_= QFileDialog.getOpenFileName(self,"Anons Yükle",os.getenv("HOME"),"Dosyası Uzantısı(*.mp3)")
		
		self.dosyaPath=path
		
		if path != "":
			self.ui.statusbar.showMessage(path+('  Şeçildi.' ))
			self.dosyaSecildi = True
			self.radioGroup.setExclusive(False)
			self.ui.radioButton_anons1.setChecked(False)
			self.ui.radioButton_anons2.setChecked(False)
			self.ui.radioButton_anons3.setChecked(False)
			self.radioGroup.setExclusive(True)
			self.ui.playButton.setEnabled(True)
			self.ui.stopButton.setEnabled(False)
			pygame.mixer.music.stop()
			self.ui.playButton.setIcon(QIcon(":\icons\icons\play.jpg"))
			self.twice_play_pause = False
			self.twiceclick=False
			
		else:
			self.ui.statusbar.showMessage("USB'den herhangi bir dosya yüklenmedi")
			self.ui.playButton.setEnabled(False)
			self.dosyaSecildi = False
			
#=======================================================================================
			
	def play_the_songs(self):

		if self.twice_play_pause:
			for event in pygame.event.get():
				if event == self.MUSIC_END:
					self.twice_play_pause = False
		if self.twice_play_pause is not True:

			self.ui.playButton.setIcon(QIcon(":\icons\icons\pause.jpg"))
			self.ui.playButton.setIconSize(QSize(45,45))

			if self.ui.radioButton_anons1.isChecked():
				tikliolan=1
			elif self.ui.radioButton_anons2.isChecked():
				tikliolan=2
			elif self.ui.radioButton_anons3.isChecked():
				tikliolan=3

			
			if self.dosyaSecildi:
				
				self.playsound = pygame.mixer.init()        
				pygame.mixer.music.load(self.dosyaPath)
				pygame.mixer.music.play()
				


			elif tikliolan==1:
				
				self.playsound =pygame.mixer.init()
				Track_1 = pygame.mixer.music.load ( "C:\\Users\\Erhan67\\Desktop\\PyCharmProjeler\\test_proje\\sound\\anons_1.mp3")
				pygame.mixer.music.play()
				#self.dosyaSecildi = False

					
			elif tikliolan==2:
				
				self.playsound =pygame.mixer.init()
				Track_2 = pygame.mixer.music.load ( "C:\\Users\\Erhan67\\Desktop\\PyCharmProjeler\\test_proje\\sound\\anons_2.mp3")
				pygame.mixer.music.play()
				#self.dosyaSecildi = False

			elif tikliolan==3:
				self.playsound =pygame.mixer.init()
				Track_3 = pygame.mixer.music.load ( "C:\\Users\\Erhan67\\Desktop\\PyCharmProjeler\\test_proje\\sound\\anons_3.mp3")
				pygame.mixer.music.play()
				#self.dosyaSecildi = False

			

			self.twice_play_pause=True
			self.ui.stopButton.setEnabled(True)
			self.MUSIC_END = pygame.USEREVENT+1
			pygame.mixer.music.set_endevent(self.MUSIC_END)
		
		else:
						
			if self.playsound is None:
				pygame.mixer.music.pause()
				self.ui.playButton.setIcon(QIcon(":\icons\icons\play.jpg"))
				self.ui.playButton.setIconSize(QSize(50,50))
				self.playsound = 1
			
			else:
			
				self.playsound = None  
				pygame.mixer.music.unpause()
				self.ui.playButton.setIcon(QIcon(":\icons\icons\pause.jpg"))
				self.ui.playButton.setIconSize(QSize(45,45))
	#=============================================================================================					
		
	def stop_the_songs(self):

		self.ui.stopButton.setIcon(QIcon(":\icons\icons\stop.jpg"))
		pygame.mixer.music.stop()
		self.ui.playButton.setEnabled(False)
		self.ui.stopButton.setEnabled(False)
		self.ui.playButton.setIcon(QIcon(":\icons\icons\play.jpg"))
		#self.ui.radioButton_anons2.setChecked(False)
				
#=============================================================================================			
	def anons1_radobutton(self):
		if self.ui.radioButton_anons1.isChecked():
			self.ui.playButton.setIcon(QIcon(":\icons\icons\play.jpg"))
			self.ui.statusbar.showMessage('Anons 1 Seçildi.')
			self.ui.playButton.setEnabled(True)
			self.ui.stopButton.setEnabled(False)
			pygame.mixer.music.stop()
			self.dosyaSecildi = False
			self.twice_play_pause = False
			self.twiceclick=False
#=============================================================================================

	def anons2_radobutton(self):
		if self.ui.radioButton_anons2.isChecked():
			self.ui.playButton.setIcon(QIcon(":\icons\icons\play.jpg"))
			self.ui.statusbar.showMessage('Anons 2 Seçildi.')
			self.ui.playButton.setEnabled(True)
			self.ui.stopButton.setEnabled(False)
			pygame.mixer.music.stop()
			self.dosyaSecildi = False
			self.twice_play_pause = False
			self.twiceclick=False
		
#=============================================================================================

	def anons3_radobutton(self):
		if self.ui.radioButton_anons3.isChecked():
			self.ui.playButton.setIcon(QIcon(":\icons\icons\play.jpg"))
			self.ui.statusbar.showMessage('Anons 3 Seçildi.')
			self.ui.playButton.setEnabled(True)
			self.ui.stopButton.setEnabled(False)
			pygame.mixer.music.stop()
			self.dosyaSecildi = False
			self.twice_play_pause = False
			self.twiceclick=False
	
#=============================================================================================
	




