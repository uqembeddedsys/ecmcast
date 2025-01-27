import os
import struct

# Framebuffer device
FB_DEVICE = "/dev/fb0"

# Screen parameters (adjust these based on your framebuffer configuration)
SCREEN_WIDTH = 800  # Replace with your screen width
BYTES_PER_PIXEL = 2  # RGB565 uses 2 bytes per pixel

# Pixel location
x = 50
y = 50

# RGB565 value for blue
blue_color = 0x07E0  # RGB565: 00000 000000 11111 (16-bit value)

# Calculate the byte offset for the pixel
offset = (y * SCREEN_WIDTH + x) * BYTES_PER_PIXEL

# Write the pixel color to the framebuffer
try:
    # Open the framebuffer device
    with open(FB_DEVICE, "r+b") as fb:
        # Seek to the correct pixel location
        fb.seek(offset)
        # Write the color (convert to bytes)
        fb.write(struct.pack('<H', blue_color))  # '<H' for little-endian 16-bit integer
    print(f"Pixel written at ({x}, {y}) with color 0x{blue_color:04X}.")
except PermissionError:
    print(f"Permission denied: Try running as root or using 'sudo'.")
except FileNotFoundError:
    print(f"Framebuffer device {FB_DEVICE} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
