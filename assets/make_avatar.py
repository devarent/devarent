"""Generate a square, circular-crop-safe GitHub avatar from scratch with Pillow.

Style matches the existing AF brand: dark navy background, subtle grid and halo,
a cyan->violet gradient rounded frame, the "AF" monogram and three accent dots.
No external image generation API is required.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SIZE = 512
OUT = "avatar.png"

# Palette
BG = (11, 15, 23)          # #0B0F17
GRID = (30, 41, 59)        # #1E293B
CYAN = (34, 211, 238)      # #22D3EE
INDIGO = (99, 102, 241)    # #6366F1
VIOLET = (168, 85, 247)    # #A855F7
FRAME = (15, 23, 42)       # #0F172A

img = Image.new("RGB", (SIZE, SIZE), BG)
px = img.load()

# Smooth diagonal gradient wash (cyan top-left -> violet bottom-right) at low alpha.
for y in range(SIZE):
    for x in range(SIZE):
        t = (x + y) / (2 * (SIZE - 1))
        r = int(CYAN[0] * (1 - t) + VIOLET[0] * t)
        g = int(CYAN[1] * (1 - t) + VIOLET[1] * t)
        b = int(CYAN[2] * (1 - t) + VIOLET[2] * t)
        # blend 12% over background
        px[x, y] = (
            int(BG[0] * 0.88 + r * 0.12),
            int(BG[1] * 0.88 + g * 0.12),
            int(BG[2] * 0.88 + b * 0.12),
        )

# Soft radial halo behind the monogram.
halo = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
hd = ImageDraw.Draw(halo)
hd.ellipse([40, 20, 472, 452], fill=(99, 102, 241, 70))
halo = halo.filter(ImageFilter.GaussianBlur(60))
img = Image.alpha_composite(img.convert("RGBA"), halo)

d = ImageDraw.Draw(img)

# Fine grid.
for i in range(0, SIZE, 32):
    d.line([(i, 0), (i, SIZE)], fill=GRID + (90,), width=1)
    d.line([(0, i), (SIZE, i)], fill=GRID + (90,), width=1)

# Corner connection accents.
for x, y, color in [(96, 140, CYAN), (96, 372, CYAN), (416, 140, VIOLET), (416, 372, VIOLET)]:
    d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=color + (255,))

# Gradient rounded frame. Implemented as a mask so the stroke follows a gradient.
frame = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
fd = ImageDraw.Draw(frame)
fd.rounded_rectangle([116, 116, 396, 396], radius=64, outline=(255, 255, 255, 255), width=4)
grad = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
gpx = grad.load()
for y in range(SIZE):
    for x in range(SIZE):
        t = (x + y) / (2 * (SIZE - 1))
        gpx[x, y] = (
            int(CYAN[0] * (1 - t) + VIOLET[0] * t),
            int(CYAN[1] * (1 - t) + VIOLET[1] * t),
            int(CYAN[2] * (1 - t) + VIOLET[2] * t),
            255,
        )
frame.putalpha(frame.getchannel("A"))
grad.putalpha(Image.composite(frame.getchannel("A"), Image.new("L", (SIZE, SIZE), 0), frame.getchannel("A")))
img = Image.alpha_composite(img, grad)

d = ImageDraw.Draw(img)
# Dark panel inside the frame for contrast.
d.rounded_rectangle([120, 120, 392, 392], radius=60, fill=(15, 23, 42, 210))

# Monogram with a vertical gradient fill.
font_path = None
for candidate in (
    "C:/Windows/Fonts/segoeuib.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "C:/Windows/Fonts/Bahnschrift.ttf",
):
    try:
        ImageFont.truetype(candidate, 140)
        font_path = candidate
        break
    except OSError:
        continue
font = ImageFont.truetype(font_path, 148) if font_path else ImageFont.load_default()

text = "AF"
box = d.textbbox((0, 0), text, font=font)
tw, th = box[2] - box[0], box[3] - box[1]
tx = (SIZE - tw) / 2 - box[0]
ty = 300 - th / 2 - box[1]

text_layer = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
td = ImageDraw.Draw(text_layer)
td.text((tx, ty), text, font=font, fill=(255, 255, 255, 255))
tmask = text_layer.getchannel("A")
tgrad = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
tpx = tgrad.load()
for y in range(SIZE):
    t = y / (SIZE - 1)
    r = int(CYAN[0] * (1 - t) + VIOLET[0] * t)
    g = int(CYAN[1] * (1 - t) + VIOLET[1] * t)
    b = int(CYAN[2] * (1 - t) + VIOLET[2] * t)
    for x in range(SIZE):
        tpx[x, y] = (r, g, b, 255)
tgrad.putalpha(tmask)
img = Image.alpha_composite(img, tgrad)

# Accent dots under the monogram.
d = ImageDraw.Draw(img)
for cx, cy, r, color in [(236, 330, 6, CYAN), (256, 330, 4, INDIGO), (276, 330, 3, VIOLET)]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (255,))

img.convert("RGB").save(OUT, "PNG", optimize=True)
print(f"wrote {OUT} ({SIZE}x{SIZE})")
