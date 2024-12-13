import os
import struct
import numpy as np
from PIL import Image

def image_to_text(image_path, output_path, binary=True):
    """Converts an image to a text or binary file storing the pixel data."""
    try:
        img = Image.open(image_path).convert('RGBA')
        width, height = img.size
        pixel_data = np.array(img)

        if binary:
            with open(output_path, 'wb') as f:
                f.write(struct.pack('ii', width, height))
                pixel_data.tofile(f)
        else:
            with open(output_path, 'w') as f:
                f.write(f'{width},{height}\n')
                for y in range(height):
                    for x in range(width):
                        r, g, b, a = pixel_data[y, x]
                        f.write(f'{x},{y}:{r},{g},{b},{a}\n')
    except Exception as e:
        print(f"Error: {e}")


def text_to_image(input_path, output_path, binary=True, output_format='png'):
    """Restores an image from a text or binary file."""
    try:
        if binary:
            with open(input_path, 'rb') as f:
                width, height = struct.unpack('ii', f.read(8))
                pixel_data = np.fromfile(f, dtype=np.uint8).reshape((height, width, 4))
        else:
            with open(input_path, 'r') as f:
                lines = f.readlines()
            width, height = map(int, lines[0].strip().split(','))
            pixel_data = np.zeros((height, width, 4), dtype=np.uint8)

            for line in lines[1:]:
                try:
                    coords, color = line.strip().split(':')
                    x, y = map(int, coords.split(','))
                    r, g, b, a = map(int, color.split(','))
                    pixel_data[y, x] = [r, g, b, a]
                except:
                    continue

        img = Image.fromarray(pixel_data, 'RGBA')
        img.save(output_path, format=output_format.upper())
    except Exception as e:
        print(f"Error: {e}")

