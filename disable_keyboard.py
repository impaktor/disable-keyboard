"""Script to grab laptop-keyboard eventss from kernel, so I can have
external keyboard ontop of my laptop keyboard without meyhem.

https://python-evdev.readthedocs.io/en/latest/tutorial.html

https://www.freedesktop.org/software/libevdev/doc/latest/group__init.html#ga5d434af74fee20f273db568e2cbbd13f
This is what I do in c
"""

import evdev

def find_device(devices, match):
    """Find device path with name that matches input"""

    for device in devices:
        if match == device.name:
            print(f"Found device path: {device.path}")
            return device.path


def get_info(dev_path='/dev/input/event6'):
    "Some debug info about device in path"
    dev = evdev.InputDevice(dev_path)
    print(f"\n {dev}\n")
    print(dev.capabilities(verbose=True))

    print("Check LED state")
    print(dev.leds(verbose=True))

    print("Check active keys")
    print(dev.active_keys(verbose=True))


# todo https://python-evdev.readthedocs.io/en/latest/apidoc.html
def getKey(dev):
    "dev - input device"
    # https://raspberrypi.stackexchange.com/questions/50007/mapping-key-events-using-evdev
    for event in dev.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            c = evdev.categorize(event)
            if c.keystate == c.key_down:
                yield c.keycode


if __name__ == "__main__":
    # Find all devices
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

    # Print info on all devices (need to run as root):
    for device in devices:
        print(f"{device.path}\t{device.name}\t{device.phys}")

    # Identified & copied from reading output of all devices:
    laptop_keyboard_name = "AT Translated Set 2 keyboard"

    # Choose path in /dev/input/<x> to keyboard device:
    # path = '/dev/input/event4'
    path = find_device(devices, laptop_keyboard_name)

    get_info(path)

    # keygenerator = getKey()

    # tpad = evdev.InputDevice('/dev/input/event11')
    keybd = evdev.InputDevice(path)

    # disable device
    keybd.grab()
    print("grabbing keyboard!")

    # Print every key pressed, hang-loop:
    for event in keybd.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            print(evdev.categorize(event))

            # ESC on the now dead keyboard kills the script and returns control
            if evdev.categorize(event).keycode == "KEY_ESC":
                break

    print("ungrabbing keyboard!")
    keybd.ungrab()
