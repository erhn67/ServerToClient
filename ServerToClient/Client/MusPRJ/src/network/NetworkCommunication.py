from  termcolor import colored
SEPARATOR_CHAR = "|||"
HEADER = 8





def send_req(req, socket_, encode=True):
    size = str(len(req)).zfill(HEADER)
    socket_.send(size.encode())

    
    sent = socket_.send(req.encode() if encode else req)
     


def recv_req(socket_, decode=True):

    try:
        size = int(str(socket_.recv(HEADER).decode()))
        x=round(size*(9.537*(10**-7)),2)
        print(uyari_renk("Beklenen Dosya Boyutu ==>"+str(x)+" MB",1))
       
        received_size = 0
        reqs = bytearray()
        while received_size < size:
            req = socket_.recv(size)
            received_size += len(req)
            reqs.extend(req)
        bytes()
       
        ret = bytes(reqs)

        x=round(len(ret) *(9.537*(10**-7)),2)
        print(uyari_renk("Alınan Dosya Boyutu ==>"+str(x)+" MB",4))

        return ret.decode() if decode else ret

    except ValueError:
        return None

def uyari_renk(mesaj,durum):
		if durum==1:
			return colored(mesaj,"green")
		elif durum==2:
			return colored(mesaj,"red")
		elif durum==3:
			return colored(mesaj,"blue")
		elif durum==4:
			return colored(mesaj,"yellow")