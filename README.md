# Generative Art

A small web app that generates unique algorithmic artwork on every request. Built with Pillow, Flask, and HTMx — no blockchain required.

## How it works

The app uses Python's `Pillow` library to draw a grid of rectangles or ellipses onto a 1000×1000px canvas. Each generation picks a random color palette, shape type, grid density, and stroke style, so no two images are ever the same. The result is served as a base64-encoded PNG directly in the browser, with no image files stored on disk between requests.

## Stack

- **Flask** — web framework and routing
- **Pillow** — image generation
- **HTMx** — partial page updates without a full reload (the "Generate another" button swaps only the canvas div)
- **Gunicorn** — WSGI server for production
- **Space Grotesk / Inter** — typography via Google Fonts

## Project structure

```
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── views.py             # Routes: / and /generate-another
│   ├── make_squares.py      # Image generation logic
│   └── templates/
│       └── home.html        # Frontend (dark mode, no Bootstrap)
├── palettes.json            # ~150 hand-curated color palettes
├── run.py                   # Entry point for local dev
├── Procfile                 # Gunicorn command for deployment
└── requirements.txt
```

## Running locally

```bash
# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the development server
python run.py
```

Then open [http://localhost:5000](http://localhost:5000).

## Deploying

The project includes a `Procfile` for platforms like Heroku or Code Capsules:

```
web: gunicorn run:app
```

No additional configuration needed.

## Image generation

Each call to `create()` in `make_squares.py` randomizes the following:

| Parameter        | Range                                              |
| ---------------- | -------------------------------------------------- |
| Grid cells       | 15 – 34 per axis                                   |
| Grid step        | Derived from cell count to always fill 1000×1000px |
| Shape type       | Rectangle or ellipse (50/50)                       |
| Shape size       | min: 20–50px, max: min + 20–100px                  |
| Stroke width     | 0 – 3px (0 means no outline)                       |
| Color palette    | 1 of ~150 palettes from `palettes.json`            |
| Background color | Random color drawn from the chosen palette         |

## Color palettes

All palettes live in `palettes.json` as arrays of RGBA values. There are around 150 palettes covering a wide range of styles — monochromatic, pastel, neon, earth tones, dark, and more. To add your own, append a 5-color array following the existing format:

```json
[
  [R, G, B, 255],
  [R, G, B, 255],
  [R, G, B, 255],
  [R, G, B, 255],
  [R, G, B, 255]
]
```

## Credits

Based on the tutorial [Build a Generative Art Application with Pillow, Flask and HTMx](https://codecapsules.io/docs/tutorials/generative-art/) by Code Capsules.
