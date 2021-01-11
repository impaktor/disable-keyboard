# Disable keyboard


## Description

Intercept (grab) kernel events from laptop keyboard at kernel level, so one can place an external keyboard on-top of laptop keyboard without it triggering key-events.

This way, one can comfortably have a stack of:
1. couch
2. human
3. laptop
4. keyboard
5. hands busily engaged with Emacs


## Installation

Depends on python and python-evdev package ([doc](https://python-evdev.readthedocs.io/en/latest/tutorial.html)) in Arch Linux.


## Usage

Run the script, which prints all devices it can find, and copy-paste the name of the device into the variable `laptop_keyboard_name` in the script:

    sudo python disable-keyboard.py


## License

Released under GPL-3
