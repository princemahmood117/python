from rembg import remove
from PIL import Image
from tkinter import Tk, filedialog
import os

root = Tk()
root.withdraw()

files = filedialog.askopenfilenames(
    title="Select Images",
    filetypes=[
        ("Images", "*.jpg *.jpeg *.png *.bmp *.webp")
    ]
)

if not files:
    print("No images selected.")
    exit()

for file in files:
    try:
        img = Image.open(file)

        result = remove(img)

        output = os.path.splitext(file)[0] + "_no_bg.png"

        result.save(output)

        print(f"✓ Saved: {output}")

    except Exception as e:
        print(f"Failed: {file}")
        print(e)

print("\nDone!")