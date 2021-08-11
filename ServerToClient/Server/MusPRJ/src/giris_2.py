from PyQt5.QtWidgets import *
from giris_sayfa_2_python import Ui_MainWindow
from PyQt5.QtGui import QIcon,QIntValidator
import random as rd
from home_3_3 import  HomePage


class GirisPage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.home_page=HomePage()
        
    
        self.ui.lineEdit_control.setValidator(QIntValidator(0,999,self)) # saçma sapan değerler girilmesini engeller. sadece 3 haneli sayı girilebilir
        self.ui.pushButton.clicked.connect(self.enter_slot)

      
        self.statusbar_bar_time     =3000 #ms cinsinden

        self.go_home_page() # sayfayı her kapatıp açtıın zaman giriş sayfasında açar

        self.showMaximized()    
#===================================================================================================
    def go_home_page(self):

        self.number1=rd.randint(0,100)
        self.number2=rd.randint(0,100)
        self.ui.lineEdit_control.clear() #ana sayfa düğmesine basıldığı zaman girilen sayıların toplamını siler
        self.ui.lineEdit_name.clear() #ana sayfa düğmesine basıldığı zaman ad  bilgilerni siler
        self.ui.lineEdit_password.clear() #ana sayfa düğmesine basıldığı zaman parola bilgilerni siler

        self.ui.label_control.setText("{} + {} = ? ".format(self.number1,self.number2))

        
#===================================================================================================
    def enter_slot(self):
        

        name=self.ui.lineEdit_name.text()
        password=self.ui.lineEdit_password.text()

        if (name=='artialti') and (password=='123456'):

            user_result_text= self.ui.lineEdit_control.text()
            
            if len(user_result_text)!=0: # Bir şey yazıp yazmadığını kontrol etmek için yazdık

                result=int(self.ui.lineEdit_control.text())
                
                if(result==self.number1+self.number2):
                    
                    self.ui.statusbar.showMessage("Giriş Başarılı",self.statusbar_bar_time)

                    self.home_page.show()
                    self.close()

            
                else:
                
                    self.show_massage("Giriş Başarısız","Girmiş olduğunuz sayı doğru değil")

                    self.go_home_page() #cevaplardan herhangi biri yanlış olursa giriş sayfasına yönlendirir.
            else:

                self.show_massage("Giriş Başarısız ","Herhangi bir sayı girmediniz")

                self.go_home_page() #cevaplardan herhangi biri yanlış olursa giriş sayfasına yönlendirir.

        else:

            self.show_massage("hatalı Giriş","Kulanıcıadı veya şifre hatalı")
            self.go_home_page() #cevaplardan herhangi biri yanlış olursa giriş sayfasına yönlendirir.


#===================================================================================================     
    def show_massage(self,title,text):

        message_box=QMessageBox(self) #ana window ikonu verir
        message_box.setIcon(QMessageBox.Warning)
        #message_box.setWindowIcon(QIcon(":/icons/icons/warning.jpg"))
        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.setStandardButtons(QMessageBox.Ok)
        button_ok=message_box.button(QMessageBox.Ok)
        button_ok.setText("Tamam")

        message_box.exec_()


#=================================================================================================== 

    def close_function(self,index):
        print("index",index)

        if (index!=0):

            self.ui.tabWidget.removeTab(index)  # giriş sayfası haricindeki tüm sayfaları 
                                                  #kapatılabilir özelliği verdik



#app = QApplication([])
#window= GirisPage()

#window.show()
#app.exec_()
    


        
       

