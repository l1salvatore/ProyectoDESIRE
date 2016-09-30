import evdev,os,signal,sys


class usb:
	def __init__(self,dev):
		self.device = evdev.InputDevice(dev)
		print(self.device)
	def obtener_evento(self):
		for event1 in self.device.read_loop():
		    for event2 in self.device.read_loop():
			if event2.type == evdev.ecodes.EV_KEY and event2.value == 1:
				 return event2.code
				#break
			    	#if event.code == evdev.ecodes.KEY_A:
				#    print('A')
				#elif event.code == evdev.ecodes.KEY_B:
				#    print('B') 
