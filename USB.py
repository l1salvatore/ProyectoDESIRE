import evdev,os,signal,sys


class usb:
	def __init__(self,dev):
		self.device = evdev.InputDevice(dev)
		print(self.device)
	def obtener_evento(self):
		for event in self.device.read():
			if event.type == evdev.ecodes.EV_KEY and event.value == 1:
					return event.code