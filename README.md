# Zo Macro
THIS is my first attempt at electronics and so I built a macro pad.I always wanted to make electronics and even if this doesn't get approved by stardance hack club I will be happy as at least I have been able to achieve something.

<img width="932" height="552" alt="image (3)" src="https://github.com/user-attachments/assets/678edb30-d294-4a82-a42e-7077546814d5" />


## Features

- 6 keys and 1 rotary encoder (knob with a push button)
- Seeed XIAO RP2040, running KMK firmware
- Each key wired directly to its own pin (no matrix)
- 3D-printed sandwich case: a top plate and a bottom tray, held together with 4 screws and heatset inserts

## Schematic

<img width="1071" height="632" alt="image (7)" src="https://github.com/user-attachments/assets/d3bdd373-4e29-4f59-913c-c1e9f6a86e54" />


## PCB

<img width="806" height="652" alt="image (6)" src="https://github.com/user-attachments/assets/193cb022-1eb4-4f6c-93c9-05a9bb397986" />
<img width="816" height="653" alt="image (5)" src="https://github.com/user-attachments/assets/05458cba-2d90-41b4-93b7-043c9315cee0" />


## Case
<img width="1428" height="790" alt="image" src="https://github.com/user-attachments/assets/36f56c34-37ec-4596-853e-51c046807921" />

<img width="1395" height="742" alt="image" src="https://github.com/user-attachments/assets/bd13ca95-a14c-48d4-96d6-3595d95765b3" />


## Keymap

| Key | Action |
| --- | --- |
| SW1 | Copy (Ctrl + C) |
| SW2 | Paste (Ctrl + V) |
| SW3 | Undo (Ctrl + Z) |
| SW5 | Cut (Ctrl + X) |
| SW6 | Save (Ctrl + S) |
| SW7 | Select all (Ctrl + A) |
| Knob turn | Volume down / up |
| Knob press | Mute |

## Bill of Materials

| Qty | Part | Notes |
| --- | --- | --- |
| 1 | Seeed XIAO RP2040 | Soldered on the back of the PCB |
| 6 | MX-style switches | |
| 6 | DSA keycaps (blank white) | |
| 1 | EC11E rotary encoder, 20 mm D-shaft | |
| 4 | M3 × 16 mm screws | |
| 4 | M3 × 5 × 4 mm heatset inserts | |
| 1 | PCB, 76.2 × 59.2 mm, 2-layer | Gerbers in `production/gerbers.zip` |
| 1 | 3D-printed top plate | `production/Top.STEP` |
| 1 | 3D-printed bottom tray | `production/Bottom.STEP` |

## Files

- `CAD/` – full assembled model (`assembled-model.STEP`)
- `PCB/` – KiCad project files
- `Firmware/` – KMK firmware (`main.py`)
- `production/` – files for manufacturing (gerbers, case STEP files, firmware)
