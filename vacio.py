import evdev

device = evdev.InputDevice('/sys/devices/pci000xyz/000.000.XYZ/usbX/X-Y')
print(device)


for event in device.read_loop():
     if event.type == evdev.ecodes.EV_KEY:
         print(evdev.categorize(event))