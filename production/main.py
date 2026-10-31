import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Volume and mute keys need the media keys extension
keyboard.extensions.append(MediaKeys())

# Each key is wired straight to its own XIAO pin (no matrix, no diodes).
# Pressing a key connects its pin to GND, so "pressed" reads as False.
KEY_PINS = (
    board.D10,  # SW1 (top row, left)
    board.D9,   # SW2 (top row, middle)
    board.D4,   # SW3 (top row, right)
    board.D7,   # SW5 (bottom row, left)
    board.D8,   # SW6 (bottom row, middle)
    board.D3,   # SW7 (bottom row, right)
)
keyboard.matrix = KeysScanner(pins=KEY_PINS, value_when_pressed=False, pull=True)

# Knob: pin A = D1, pin B = D2, push button = D0
encoder = EncoderHandler()
encoder.pins = ((board.D1, board.D2, board.D0, False),)
keyboard.modules.append(encoder)

# What each key does, in the same order as KEY_PINS
keyboard.keymap = [
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Z),  # SW1 copy, SW2 paste, SW3 undo
        KC.LCTL(KC.X), KC.LCTL(KC.S), KC.LCTL(KC.A),  # SW5 cut,  SW6 save,  SW7 select all
    ]
]

# Knob: turn left = volume down, turn right = volume up, press = mute.
# If it turns the wrong way once built, swap KC.VOLD and KC.VOLU.
encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
]

if __name__ == "__main__":
    keyboard.go()
