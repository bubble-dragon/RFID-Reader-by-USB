import evdev
from evdev import InputDevice, categorize, ecodes

ID = ''
# device = InputDevice("/dev/input/event0") # my keyboard
dev = InputDevice('/dev/input/event0')
scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0'
}
for event in dev.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        data = evdev.categorize(event)  # Save the event temporarily to introspect it
        if data.keystate == 1:  # Down events only
            key_lookup = str(scancodes.get(data.scancode))
            if key_lookup == 'None': print(ID)
            else: ID += key_lookup