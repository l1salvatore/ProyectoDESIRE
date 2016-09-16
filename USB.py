import evdev,os,signal,sys


class usb:
	def __init__(self,dev):
		self.device = evdev.InputDevice(dev)
		print(self.device)
	def escuchar(self):
		os.system("stty -echo")
		for event in self.device.read_loop():
			if event.type == evdev.ecodes.EV_KEY:
				if event.code == evdev.ecodes.KEY_A and event.value == 1:
					print("una A presionada\n")
				elif event.code == evdev.ecodes.KEY_B and event.value == 1:
					print("una B presionada\n")