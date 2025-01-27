import sys

def rgb888_to_rgb565(rgb_data):
    rgb565_data = bytearray()
    for i in range(0, len(rgb_data), 3):
        r = rgb_data[i]   # Red
        g = rgb_data[i+1] # Green
        b = rgb_data[i+2] # Blue

        # Convert RGB888 to RGB565
        rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)

        # Append as two bytes (big-endian)
        rgb565_data.append((rgb565 >> 8) & 0xFF)  # High byte
        rgb565_data.append(rgb565 & 0xFF)         # Low byte

    return rgb565_data

if len(sys.argv) != 3:
    print("Usage: python3 rgb888_to_rgb565.py <input.raw> <output.rgb565>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the RGB888 raw data
with open(input_file, "rb") as f:
    rgb888_data = f.read()

# Convert to RGB565
rgb565_data = rgb888_to_rgb565(rgb888_data)

# Write the RGB565 data to output
with open(output_file, "wb") as f:
    f.write(rgb565_data)

print(f"Converted {input_file} to {output_file} in RGB565 format.")
