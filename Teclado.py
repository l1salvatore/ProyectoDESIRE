import USB,evdev,threading,sys

global codigo
codigo = ""

class Teclado:
	def __init__(self,port):
		self.puerto = USB.usb(port)
	def iniciar_teclado(self):
		p = threading.Thread(target=self.puerto.obtener_evento,args=(codigo,))
	        p.start()
		while 1:
		    if codigo == evdev.ecodes.KEY_A:
			print('A')
		    elif codigo == evdev.ecodes.KEY_B:
			print('B')
