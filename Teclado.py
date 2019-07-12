import USB,evdev,threading,sys,time
from collections import defaultdict

{- Merge test -}adada

teclas = { evdev.ecodes.KEY_A : 'A',
	   evdev.ecodes.KEY_B : 'B',
	   evdev.ecodes.KEY_C : 'C',
	   evdev.ecodes.KEY_D : 'D',
	   evdev.ecodes.KEY_E : 'E',
	   evdev.ecodes.KEY_F : 'F',
	   evdev.ecodes.KEY_G : 'G',
	   evdev.ecodes.KEY_H : 'H',
	   evdev.ecodes.KEY_I : 'I',
	   evdev.ecodes.KEY_J : 'J',
	   evdev.ecodes.KEY_K : 'K',
	   evdev.ecodes.KEY_L : 'L',
	   evdev.ecodes.KEY_M : 'M',
	   evdev.ecodes.KEY_N : 'N',
	   evdev.ecodes.KEY_O : 'O',
	   evdev.ecodes.KEY_P : 'P',
	   evdev.ecodes.KEY_Q : 'Q',
	   evdev.ecodes.KEY_R : 'R',
	   evdev.ecodes.KEY_S : 'S',
	   evdev.ecodes.KEY_T : 'T',
	   evdev.ecodes.KEY_U : 'U',
	   evdev.ecodes.KEY_V : 'V',
	   evdev.ecodes.KEY_W : 'W',
	   evdev.ecodes.KEY_X : 'X',
	   evdev.ecodes.KEY_Y : 'Y',
	   evdev.ecodes.KEY_Z : 'Z',
	   evdev.ecodes.KEY_F1 : "F1"}

teclas = defaultdict(lambda: "UNKNOWN", teclas)


class Teclado:
	def __init__(self,port):
		self.puerto = USB.usb(port)
	def esperar_tecla(self):
		ev = self.puerto.obtener_evento()
		return teclas[ev]
