import evdev,os,signal,sys


class usb:
	def __init__(self,dev):
		self.device = evdev.InputDevice(dev)
		print(self.device)
	def obtener_evento(self,codigo):
		for event in self.device.read_loop():
			if event.type == evdev.ecodes.EV_KEY and event.value == 1:
				codigo = event.code
			    	#if event.code == evdev.ecodes.KEY_A:
				#    print('A')
				#elif event.code == evdev.ecodes.KEY_B:
				#    print('B') 
