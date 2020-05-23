"""Script to grab laptop-keyboard eventss from kernel, so I can have
external keyboard ontop of my laptop keyboard without meyhem.

https://python-evdev.readthedocs.io/en/latest/tutorial.html

https://www.freedesktop.org/software/libevdev/doc/latest/group__init.html#ga5d434af74fee20f273db568e2cbbd13f
This is what I do in c

"Grab or ungrab the device through a kernel EVIOCGRAB.
This prevents other clients (including kernel-internal ones such as rfkill) from receiving events from this device.
This is generally a bad idea. Don't do this."

"""

import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

# Print info on all devices (need to run as root):
[print(f"{device.path}\t{device.name}\t{device.phys}") for device in devices]


def get_info(dev_path='/dev/input/event6'):
    "Some debug info about device in path"
    dev = evdev.InputDevice(dev_path)
    print(f"\n {dev}\n")
    print(dev.capabilities(verbose=True))

    print("Check LED state")
    print(dev.leds(verbose=True))

    print("Check active keys")
    print(dev.active_keys(verbose=True))


# choose path to keyboard device
path = '/dev/input/event6'

# tpad = evdev.InputDevice('/dev/input/event11')
keybd = evdev.InputDevice(path)

# disable device
keybd.grab()
print("grabbing keyboard!")

# Print every key pressed, hang-loop:
for event in keybd.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
        # find if "KEY_ESC"

print("ungrabbing keyboard!")
keybd.ungrab()
