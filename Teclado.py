import USB,evdev,threading,sys,time

#global codigo
#codigo = [1]
#global flag
#flag = threading.Event()

class Teclado:
	def __init__(self,port):
		self.puerto = USB.usb(port)
	def esperar_tecla(self):
		ev = self.puerto.obtener_evento()
		if ev == evdev.ecodes.KEY_A:
			return 'A'
		elif ev == evdev.ecodes.KEY_U:
			return 'U'
		elif ev == evdev.ecodes.KEY_C:
			return 'C'
