import socket
import threading
import _thread
import sys,os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from src.music_utils import Song
from src.network import NetworkCommunication
from src.utils import Constants


from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication,QFileDialog,QWidget,QMessageBox,QButtonGroup
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import *
from home_3_3 import HomePage

from queue import Queue
import threading
import _thread
from termcolor import colored
from time import sleep



class MultiServer():
	def __init__(self):
		super().__init__()
		
		self.ui=None

		self.dosyaSecildi = False
		self.dosyaPath = ""
		self.send_song=None

		self.twiceclick=False
		self.twice_play_pause=False
		self.clicked_list_twice=False
		self.playsound=None
		self.pause=None

		
		self.sock=None
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.conn=True
		self.msg_1=None

		self.server.bind(('', Constants.PORT))
		self.server.listen(20)
		self.pushbutton_list=[]
		self.clients = []
		self.address = []
		self.clicked_list = []
		self.clicked_list_2=[]

		self.DeviceButtonIndx=0
		self.hoparlor_ip_list= [['192.168.5.141',0],['192.168.5.142',1],['127.0.0.1',2],['192.168.5.155',3],
								['192.168.5.156',4],['192.168.5.157',5],['192.168.5.158',6],['192.168.5.159',7]]


		


		self.a="Hoparlor seçimedi.Lütfen Hoparlöri siteme bağlayınız..."

		self.songs = Song.get_songs(Constants.PATH_TO_MUSIC_LIB)

		self.t2= threading.Thread(target=self.arayuz_calistir)
		self.sock_send_msg_thread=threading.Thread(target=self.sock_send_msg)

		print(self.uyari_renk("[+] Server Başlatıldı.",1))
		print(self.uyari_renk("[+] Gelen bağlantılar bekleniliyor...",1))
		
	def uyari_renk(self,mesaj,durum):
		if durum==1:
			return colored(mesaj,"green")
		elif durum==2:
			return colored(mesaj,"red")
		elif durum==3:
			return colored(mesaj,"blue")
		elif durum==4:
			return colored(mesaj,"yellow")



	def accept(self):

		done = False
		while not done:

			try:
				sock, adres = self.server.accept()
				adres = adres + (str(sock.recv(4096), "utf-8"),)
				

				self.clients.append(sock)
				self.address.append(adres)

				_thread.start_new_thread(self.recv_msg, (sock,))
				_thread.start_new_thread(self.sock_send_msg, (sock,))	

				print("1. işlem")
				
				print(str(self.uyari_renk("\n[+] " + adres[0] +   " den bağlantı kuruldu",1)))

				
				self.listele_2() # Aktif olan Hoparlörleri Gösterir

			
			except OSError:
				print("2.işlem")
				done = True
				continue

	def DeviceButtonsCommonHandler(self):
		
		print("OO basıldı")
		print ("Tus=["+str(self.DeviceButtonIndx)+"]"+" IP=["+str(self.hoparlor_ip_list[self.DeviceButtonIndx])+"]")
		try:
	
			f = False
			i=0
			
			for adres in self.address:

				if adres[0]==self.hoparlor_ip_list[self.DeviceButtonIndx][0]:
				 	self.conn=False

				if self.hoparlor_ip_list[self.DeviceButtonIndx][0] in adres[0]:
					f=True
					break
				i+=1
					
							
			if self.conn is not True and f:
				print("basıldı_3")
				self.sonuc=''
				if self.pushbutton_list[self.DeviceButtonIndx].isChecked()==1:
					
					print(self.uyari_renk("\n"+ self.hoparlor_ip_list[self.DeviceButtonIndx][0] +" aktif edildi",1))
					self.clicked_list.append(self.clients[i]) 
					self.pushbutton_list[self.DeviceButtonIndx].setStyleSheet("border-image: url(:/icons/icons/koyu_yesil.jpg);")
					self.label_haporlor_list[self.DeviceButtonIndx].setStyleSheet("color:green")
					print(str(self.uyari_renk("\n[+] " + "Aktif olan Hoparlörler..: \n"+"\n",4)))
					self.listele()
	
				else:
					
					print(self.uyari_renk("\n"+self.hoparlor_ip_list[self.DeviceButtonIndx][0]+ " pasif edildi",2))
					self.clicked_list.remove(self.clients[i])
					self.pushbutton_list[self.DeviceButtonIndx].setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
					self.label_haporlor_list[self.DeviceButtonIndx].setStyleSheet("color: rgb(170, 0, 0);")
					print(str(self.uyari_renk("\n[+] " + "Aktif olan Hoparlörler..: \n"+"\n",4)))
					self.listele()

			else:
				
				print(self.uyari_renk(self.a,2))
				self.pushbutton_list[self.DeviceButtonIndx].setChecked(False)
				print(str(self.uyari_renk("\n[+] " + "Aktif olan Hoparlörler..: \n"+"\n",4)))
				self.listele()
		except UnboundLocalError:
			return None 
		
		except ValueError:

			return None

		except IndexError:
			return None

	def recv_msg(self,sock): 

		done=False
		while not done:
			
			try:
				self.msg_1 =NetworkCommunication.recv_req(sock, decode=False)
				if self.msg_1 != None:

					print(str(self.uyari_renk("\n[+] " + "Alınan Mesaj..: "+str(self.msg_1)+"\n",1)))
			
			except ConnectionAbortedError:
				done= True	
				self.listele_2()
				
	def sock_send_msg(self,sock):
		
		done=False

		while not done:

			for index,sock in  enumerate(self.clients):
				try:
					NetworkCommunication.send_req("Merhaba "+str(self.address[index][0]),self.clients[index], encode=True)
					sleep(4)

				except ConnectionAbortedError:

					done=True
				except ConnectionResetError:
					done=True
				#continue
#=============================================================================================

	def hoparlor_1_clicked(self):
			self.DeviceButtonIndx=0		
			self.DeviceButtonsCommonHandler()
			
			return None
	def hoparlor_2_clicked(self):
			self.DeviceButtonIndx=1		
			self.DeviceButtonsCommonHandler()
		
			return None
	def hoparlor_3_clicked(self):
			self.DeviceButtonIndx=2		
			self.DeviceButtonsCommonHandler()
			return None
	def hoparlor_4_clicked(self):
			self.DeviceButtonIndx=3		
			self.DeviceButtonsCommonHandler()
			return None
	def hoparlor_5_clicked(self):
			self.DeviceButtonIndx=4		
			self.DeviceButtonsCommonHandler()
			return None
	def hoparlor_6_clicked(self):
			self.DeviceButtonIndx=5		
			self.DeviceButtonsCommonHandler()
			return None
	def hoparlor_7_clicked(self):
			self.DeviceButtonIndx=6		
			self.DeviceButtonsCommonHandler()
			return None
	def hoparlor_8_clicked(self):
			self.DeviceButtonIndx=7		
			self.DeviceButtonsCommonHandler()
			return None
		

	def arayuz_calistir(self):
		uygulama = QApplication([])
		self.window = HomePage()
		self.window.show()
		self.ui = self.window.ui

		self.label_haporlor_list=[self.ui.label_hoparlor_1,self.ui.label_hoparlor_2,
									self.ui.label_hoparlor_3,self.ui.label_hoparlor_4,
									self.ui.label_hoparlor_5,self.ui.label_hoparlor_6,
									self.ui.label_hoparlor_7,self.ui.label_hoparlor_8]


		self.pushbutton_list=[self.ui.pushButton_hoparlor_1,self.ui.pushButton_hoparlor_2,
								self.ui.pushButton_hoparlor_3,self.ui.pushButton_hoparlor_4,
								self.ui.pushButton_hoparlor_5,self.ui.pushButton_hoparlor_6,
								self.ui.pushButton_hoparlor_7,self.ui.pushButton_hoparlor_8]


		for index in range(0,len(self.pushbutton_list)):
			self.pushbutton_list[index].setCheckable(True)


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
		
		
		self.ui.pushButton_ses_gonder.clicked.connect(self.yazdir_clicked)

		self.ui.pushButton_usbden_yukle.clicked.connect(self.usbden_yukle)

		self.ui.stopButton.setEnabled(False)
		self.ui.acilButton.setEnabled(True)
		

		self.ui.acilButton.clicked.connect(self.acil_song)
		self.ui.stopButton.clicked.connect(self.stop_the_songs)
		
		uygulama.exec_()
#=============================================================================================
	

#=============================================================================================		
	def listele(self,durum=True):
		sonuc = ''
		for i, sock in enumerate(self.clicked_list):
			try:
				sock.send(str.encode(" "))
				
			except Exception:
				
				del self.clicked_list[i]
				
				print(" listele")

				continue
			if durum:
				sonuc += str(i) + "\t"+str(self.address[i][0]) + "\t" + str(self.address[i][1]) + "\t" + str(self.address[i][2]) + "\n"
		if durum:
			print(self.uyari_renk("*_______________Hoparlör Listesi________________*",3))
			print(self.uyari_renk("index\tIp Adresi\tPort\tAlınan Mesaj",3))
			print(self.uyari_renk(sonuc,1))
#=============================================================================================
	def listele_2(self,durum=True):
		sonuc = ''
		
		for i, sock in enumerate(self.clients,start=0):
			try:
				NetworkCommunication.send_req(" ",sock, encode=True)

				#sock.send(str.encode(" "))
				print("nbr")
			
			except Exception:

				del self.clients[i]
				del self.address[i]
				print(i)

				print(self.uyari_renk(str(self.hoparlor_ip_list[i][0]) +" Bağlantısı koptu",2))
			
			
			
					
				# if self.address[i][0]==self.hoparlor_ip_list[i]:
				# 	self.pushbutton_list[self.DeviceButtonIndx].setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
				# 	self.label_haporlor_list[self.DeviceButtonIndx].setStyleSheet("color: rgb(170, 0, 0);")
				# if self.address[i][0]==self.hoparlor_ip_list[i] and  self.pushbutton_list[i].isChecked()==1:
					 
				# 	self.pushbutton_list[i].setStyleSheet("border-image: url(:/icons/icons/koyu_kirmizi.jpg);")
				# 	self.label_haporlor_list[i].setStyleSheet("color: rgb(170, 0, 0);")

				print("ikinci işlem listele_2")

				continue
			if durum:
				sonuc += str(i) + "\t"+str(self.address[i][0]) + "\t" + str(self.address[i][1]) + "\t" + str(self.address[i][2]) + "\n"
		if durum:
			print(str(self.uyari_renk("\n[+] " + "Aktif olan Hoparlörler..: \n",4)))
			print(self.uyari_renk("index\tIp Adresi\tPort\tAlınan Mesaj",3))
			print(self.uyari_renk(sonuc,1))

	def yazdir_clicked(self,durum=True):

		tikliolan = 0
		if self.ui.radioButton_anons1.isChecked():
			tikliolan=1		
		elif self.ui.radioButton_anons2.isChecked():
			tikliolan=2
		elif self.ui.radioButton_anons3.isChecked():
			tikliolan=3
		elif self.dosyaSecildi:
			self.dosyaPath

		if self.twiceclick is not True:
			

			if len(self.clicked_list) == 0 and tikliolan == 0 and self.dosyaPath=="":
				print(self.clicked_list)
				self.window.show_massage("Hatalı Giriş","Hoparlor ve Anons seçilmedi.")
				return
			elif len(self.clicked_list) == 0:
				self.window.show_massage("Hatalı Giriş","Hoparlor seçilmedi ")
				return
			
			elif tikliolan == 0 and self.dosyaPath=="":
				self.window.show_massage("Hatalı Giriş","Anons seçilmedi ")
				return

			sonuc = ''
			for index,sock in enumerate(self.clicked_list):

				try:
					sock.send(str.encode(" "))
					#self.clicked_list[index]
					#self.address[index]
				except Exception:
					print("yazdır")
					
					#del self.clicked_list[index]
					#del self.address[index]
					continue
				sonuc += str(index) + "\t" + str(self.address[index][0]) + "\t" + str(self.address[index][1]) +  "\n"
				print(self.uyari_renk("*_____Anonsların Gönderildiği Hoparlör_____*",3))
				print(self.uyari_renk("index\tIp Adresi\tPort\t",3))
				print(self.uyari_renk(sonuc,1))
				
				
					
				NetworkCommunication.send_req(self.send_song,self.clicked_list[index], encode=False)
	
				
				x=round(len(self.send_song)*(9.537*(10**-7)),2)
				print(self.uyari_renk("Gönderilen Dosyanın Boyutu....: "+str(x)+ " MB",4))
				
				

			self.twiceclick=True

		else:				
			self.ui.statusbar.showMessage("Aynı Anons 2. kez gönderilemez ",3000)
			self.window.show_massage("Hatalı Giriş","Aynı Anons 2. kez gönderilemez ")
	#=======================================================================================
			
				
	def acil_song(self):

		self.ui.stopButton.setEnabled(True)
		s = Song.Song(file=os.path.join(Constants.PATH_TO_MUSIC_LIB,"polis.mp3"))
		self.send_song= s.get()

		
		sonuc = ''
		for index,sock in enumerate(self.clicked_list):

			try:
				sock.send(str.encode(" "))
			except Exception:
				#del self.clients[index] 
				#del self.address[index]
				continue
			
			sonuc += str(index) + "\t" + str(self.address[index][0]) + "\t" + str(self.address[index][1]) + "\t" + str(self.address[index][2]) + "\n"
			print(self.uyari_renk("*_______________Anonsların Gönderildiği Hoparlör________________*",3))
			print(self.uyari_renk("index\tIp Adresi\tPort\tHostname",3))
			print(self.uyari_renk(sonuc,1))

			NetworkCommunication.send_req("acil",self.clicked_list[index], encode=True)
			NetworkCommunication.send_req(self.send_song,self.clicked_list[index], encode=False)
			x=round(len(self.send_song)*(9.537*(10**-7)),2)
			print(self.uyari_renk("Gönderilen Dosyanın Boyutu....: "+str(x)+ " MB",4))

			self.radioGroup.setExclusive(False)
			self.ui.radioButton_anons1.setChecked(False)
			self.ui.radioButton_anons2.setChecked(False)
			self.ui.radioButton_anons3.setChecked(False)
			self.radioGroup.setExclusive(True)

			self.ui.statusbar.showMessage('Acil Anons Çalıyor...')
			

		
		self.dosyaSecildi = False
		self.twice_play_pause = False
		self.twiceclick=False	
#=============================================================================================	
	def stop_the_songs(self):

		
		for index,sock in enumerate(self.clicked_list):
			NetworkCommunication.send_req("stop",self.clicked_list[index], encode=True)
			
		self.ui.stopButton.setIcon(QIcon(":\icons\icons\stop.jpg"))
		
#=============================================================================================
	def usbden_yukle(self):

		import os
		import ntpath
		self.playsound=None
		path  = self.window.getPath()
		self.dosyaPath=path
		
		if path != "":
			s = Song.Song(file=path)
			self.send_song= s.get()
			self.ui.statusbar.showMessage(path+('  Şeçildi.' ))
			self.dosyaSecildi = True
			self.radioGroup.setExclusive(False)
			self.ui.radioButton_anons1.setChecked(False)
			self.ui.radioButton_anons2.setChecked(False)
			self.ui.radioButton_anons3.setChecked(False)
			self.radioGroup.setExclusive(True)
			self.ui.stopButton.setEnabled(True)
			
			
			self.twice_play_pause = False
			self.twiceclick=False
			
		else:
			
			self.ui.statusbar.showMessage("USB'den herhangi bir dosya yüklenmedi")
			
			self.dosya=False
			self.send_song=None


#=======================================================================================================

	def anons1_radobutton(self):
		if self.ui.radioButton_anons1.isChecked():
			
			#self.stop_the_songs()
			self.ui.statusbar.showMessage('Anons 1 Seçildi.')
			self.ui.stopButton.setEnabled(True)
			
			s = Song.Song(file=os.path.join(Constants.PATH_TO_MUSIC_LIB,"anons_1.mp3"))
			self.send_song= s.get()
			
			self.dosyaSecildi = False
			self.twice_play_pause = False
			self.twiceclick=False
#=============================================================================================

	def anons2_radobutton(self):
		if self.ui.radioButton_anons2.isChecked():
			
			self.ui.statusbar.showMessage('Anons 2 Seçildi.')
			self.ui.stopButton.setEnabled(True)
			#self.stop_the_songs()
			s = Song.Song(file=os.path.join(Constants.PATH_TO_MUSIC_LIB,"anons_2.mp3"))
			self.send_song= s.get()
			
			self.dosyaSecildi = False
			self.twice_play_pause = False
			self.twiceclick=False
		
#=============================================================================================

	def anons3_radobutton(self):
		if self.ui.radioButton_anons3.isChecked():
			
			self.ui.statusbar.showMessage('Anons 3 Seçildi.')
			self.ui.stopButton.setEnabled(True)
			#self.stop_the_songs()
			s = Song.Song(file=os.path.join(Constants.PATH_TO_MUSIC_LIB,"anons_3.mp3"))
			self.send_song= s.get()
			
			self.dosyaSecildi = False
			self.twice_play_pause = False
			self.twiceclick=False
#=============================================================================================			
	def run(self):
			
		self.t2.start()
		self.accept()
#=============================================================================================
	def close(self):
		self.server.close()
	
#=============================================================================================

if __name__ == '__main__':
	
	try:

		MultiServer().run()

	except:

		sys.exit()