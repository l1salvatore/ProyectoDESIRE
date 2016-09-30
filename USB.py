import evdev,os,signal,sys


class usb:
	def __init__(self,dev):
		self.device = evdev.InputDevice(dev)
		print(self.device)
	def obtener_evento(self):
		for event1 in self.device.read_loop():
		   # for event2 in self.device.read_loop():
			if event1.type == evdev.ecodes.EV_KEY and event1.value == 1:
				 return event1.code
