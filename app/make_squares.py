import base64
import json
import random
import io

from PIL import Image, ImageDraw

palettes = []
with open("palettes.json") as f:
    ps = json.load(f)
    for p in ps:
        palette = [tuple(x) for x in p]
        palettes.append(palette)

def create(save_path):
    colors = random.choice(palettes)
    bg_color = random.choice(colors)

    img = Image.new("RGBA", (1000, 1000), bg_color)
    d = ImageDraw.Draw(img)

    num_recs = random.randrange(15, 35)
    min_size = random.randrange(20, 50)
    max_size = min_size + random.randrange(20, 100)
    stroke_width = random.randrange(0, 4)  # 0 = sin borde
    grid_step = random.randrange(30, 80)   # grilla variable
    use_circles = random.random() > 0.5    # 50% chance de círculos

    outline = (0, 0, 0, 255) if stroke_width > 0 else None

    xoffset = 0
    yoffset = 0
    for row in range(num_recs):
        for rec in range(num_recs):
            topleftx = random.randrange(0, grid_step) + xoffset
            toplefty = random.randrange(0, grid_step) + yoffset
            bottomrightx = topleftx + random.randrange(min_size, max_size)
            bottomrighty = toplefty + random.randrange(min_size, max_size)
            color = random.choice(colors)
            xoffset += grid_step

            coords = [topleftx, toplefty, bottomrightx, bottomrighty]
            if use_circles:
                d.ellipse(coords, fill=color, outline=outline, width=stroke_width)
            else:
                d.rectangle(coords, fill=color, outline=outline, width=stroke_width)

        yoffset += grid_step
        xoffset = 0

    img.save(save_path)
    image = io.BytesIO()
    img.save(image, "PNG")
    image.seek(0)
    return base64.b64encode(image.getvalue()).decode()