import sys
import os
from PIL import Image

TARGET = 100 * 1024

if len(sys.argv) < 2:
    print("Usage: python3 compress.py input.jpg [output.jpg]")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) > 2 else "compressed.jpg"

img = Image.open(input_file).convert("RGB")

for scale in [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]:
    width = max(1, int(img.width * scale))
    height = max(1, int(img.height * scale))

    resized = img.resize((width, height), Image.Resampling.LANCZOS)

    for quality in range(60, 14, -5):
        resized.save(output_file, "JPEG", quality=quality, optimize=True)

        if os.path.getsize(output_file) <= TARGET:
            print("Success!")
            print("Output:", output_file)
            print("Size:", os.path.getsize(output_file) / 1024, "KB")
            print("Quality:", quality)
            print("Dimensions:", width, "x", height)
            sys.exit(0)

print("Could not reach 100 KB.")
