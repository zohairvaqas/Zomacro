# Zo Macro

<!-- WRITE THIS YOURSELF: 1–3 sentences about what Zo Macro is and why you made it. -->

<!-- Drag your "case-angle" screenshot here -->

## Features

- 6 keys and 1 rotary encoder (knob with a push button)
- Seeed XIAO RP2040, running KMK firmware
- Each key wired directly to its own pin (no matrix)
- 3D-printed sandwich case: a top plate and a bottom tray, held together with 4 screws and heatset inserts

## Schematic

<!-- Drag your schematic screenshot here -->

## PCB

<!-- Drag your PCB screenshot (the one with the red copper lines) here -->

<!-- Optional: drag your 3D view of the PCB here -->

## Case

<!-- Drag your "plate-top" and "tray-inside" screenshots here -->

<!-- WRITE THIS YOURSELF: 1–2 sentences on how the case fits together. -->

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
