import USB,evdev,threading,sys,time

#global codigo
#codigo = [1]
#global flag
#flag = threading.Event()

class Teclado:
	def __init__(self,port):
		self.puerto = USB.usb(port)
	def esperar_tecla(self):
		#p = threading.Thread(target=self.puerto.obtener_evento,args=(codigo,flag))
	        #p.start()
		ev = self.puerto.obtener_evento()
		if ev == evdev.ecodes.KEY_A:
			print('A')
		elif ev == evdev.ecodes.KEY_B:
			print('B')
