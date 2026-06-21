from app import app
from flask import render_template, send_file, request
from app.make_squares import create
import io, base64
from PIL import Image
import os

tmp_file_path = "/tmp/imgnew.png"

@app.route("/", methods=["GET"])
def index():
    graphic_image = create(tmp_file_path)
    return render_template("home.html", image=graphic_image)

@app.route("/generate-another", methods=["GET"])
def generate_another():
    graphic_image = create(tmp_file_path)
    response = f"""
    <div id="image-update-div">
      <div class="canvas-frame">
        <img id="new-image" src="data:image/png;base64,{graphic_image}" alt="Generated artwork" />
      </div>
      <div class="controls">
        <a class="btn btn-primary" download="art.png" href="data:image/png;base64,{graphic_image}">
          Download
        </a>
        <button
          class="btn btn-ghost"
          hx-target="#image-update-div"
          hx-get="/generate-another"
          hx-swap="outerHTML">
          Generate another
        </button>
      </div>
    </div>
    """
    return response