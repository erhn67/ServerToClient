import os,sys
import _thread
import threading
from time import sleep
import shutil
import socket
import vlc
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from src.network import NetworkCommunication
from src.utils import Constants
from termcolor import colored

class Client:
	def __init__(self, net_info: tuple):
		self.net_info = net_info
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.actu_song = None
		self.acil = False

		self.send_message = threading.Thread(target=self.send_msg)

		self.init_cache()

	def uyari_renk(self,mesaj,durum):
		if durum==1:
			return colored(mesaj,"green")
		elif durum==2:
			return colored(mesaj,"red")
		elif durum==3:
			return colored(mesaj,"blue")
		elif durum==4:
			return colored(mesaj,"yellow")

	def init_cache(self):
		done = False
		print(Constants.CACHE_PATH)
		while not done:
			try:
				os.makedirs(Constants.CACHE_PATH)
				done = True

			except FileExistsError:
				shutil.rmtree(Constants.CACHE_PATH)
				done = False
			

	def write_to_cache(self, song):
		path = os.path.join(Constants.CACHE_PATH, Constants.MUS_STREAM_FILE)
		music_file = open(path, 'wb')
		music_file.write(song)
	
	def play(self, song):
		if song is not None:
			if self.actu_song is not None:
				self.actu_song.stop()
			sleep(2)
			self.write_to_cache(song)
			self.actu_song = vlc.MediaPlayer(os.path.join(Constants.CACHE_PATH, Constants.MUS_STREAM_FILE))
			self.actu_song.play()
			

	
	def play_acil(self, song):
		if song is not None:
			if self.actu_song is not None:
				self.actu_song.stop()
			
			self.write_to_cache(song)
			self.actu_song = vlc.MediaPlayer(os.path.join(Constants.CACHE_PATH, Constants.MUS_STREAM_FILE))	
			while self.acil:
				if not self.actu_song.is_playing():
					print(self.uyari_renk("Acil Anonsu Başlatıldı.!",3))
					self.actu_song = vlc.MediaPlayer(os.path.join(Constants.CACHE_PATH, Constants.MUS_STREAM_FILE))
					self.actu_song.play()
					print(self.uyari_renk("kontrol",1))
					sleep(1)
				else:
					print(self.uyari_renk("kontrol2",1))
					sleep(1)
			self.actu_song.stop()
			print(self.uyari_renk("Acil Anonsu Bitti.",4))

	def stop(self, song):
		self.acil = False
		if song is not None:
			if self.actu_song is not None:
				self.actu_song.stop()
				print(self.uyari_renk("Anons Durduruldu",2))
			if song != "stop":
				self.write_to_cache(song)
				self.actu_song = vlc.MediaPlayer(os.path.join(Constants.CACHE_PATH, Constants.MUS_STREAM_FILE))
				self.actu_song.stop()


	def send_msg(self):
		done=False
		
		while not done:
			try: 
				self.msg_2="Hoparlör 2 bağlı..."
				self.sock.sendall(self.msg_2.encode())
				sleep(5)


			except ConnectionResetError:
				
				done=True
	

	def run(self):
		
		done_2=False
		while not done_2:
			try:
				self.sock.connect(self.net_info)
				print(self.uyari_renk("Sunucuyla Bağlantı Yapıldı..",1))
				
				self.send_message.start()
				
				done = False
				while not done:

					try:
					
						mesaj = NetworkCommunication.recv_req(self.sock, decode=False)
						if mesaj != None:
							try:
								if mesaj.decode() == "stop":
									self.stop("stop")
									

								elif  mesaj.decode() == "acil":
									self.stop("stop")
									self.acil = True
									print(self.uyari_renk("Acil Anonsu Alındı.",4))
									
							except UnicodeDecodeError:
								#print(self.uyari_renk(e,4))
								if  self.acil:
									_thread.start_new_thread(self.play_acil,(mesaj,))
								else:
									print(self.uyari_renk("Anons Başlatıldı",1))
									self.play(mesaj)
									
					except ConnectionResetError:
						print(self.uyari_renk("Sunucu Bağlantısı Koptu...",2))
						
						try:
							
							self.actu_song.stop()
							self.acil=False
						except AttributeError:
							pass
						except PermissionError:
							pass

						Client((Constants.IP, Constants.PORT)).run()
						
						done = True
						
						
			except ConnectionRefusedError:
				
				
				print(self.uyari_renk("Bağlantı zamanaşımına  uğradı! Sunucu bağlantısı yeniden sağlanıyor...",4))
				sleep(1)
				done_2=False
				
				

if __name__ == "__main__":
	Client((Constants.IP, Constants.PORT)).run()

	

	
