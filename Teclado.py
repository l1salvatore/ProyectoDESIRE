import USB,evdev

class Teclado:
	def __init__(self,port):
		self.puerto = USB.usb(port)
	def scanf(self):
		eventcode = self.puerto.obtener_evento()
		if eventcode == evdev.ecodes.KEY_A:
			return 'A'
		elif eventcode == evdev.ecodes.KEY_B:
			return 'B' 