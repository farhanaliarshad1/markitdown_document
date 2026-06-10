import os
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
from markitdown import MarkItDown

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
ALLOWED_EXTENSIONS = {
    "pdf",
    "pptx", "ppt",
    "docx", "doc",
    "xlsx", "xls",
    "jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp",
    "mp3", "wav", "m4a", "ogg", "flac",
    "html", "htm",
    "csv", "json", "xml",
    "zip",
    "epub",
}

app = Flask(__name__)
app.secret_key = "markitdown-secret-key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50 MB limit


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("No file part in the request.", "error")
        return redirect(url_for("index"))

    file = request.files["file"]

    if file.filename == "":
        flash("No file selected.", "error")
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        flash("Unsupported file type.", "error")
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(pdf_path)

    md_filename = os.path.splitext(filename)[0] + ".md"
    md_path = os.path.join(app.config["UPLOAD_FOLDER"], md_filename)

    try:
        result = MarkItDown().convert(pdf_path)
        md_content = result.text_content
    except Exception as exc:
        flash(f"Conversion failed: {exc}", "error")
        return redirect(url_for("index"))

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    return send_file(
        md_path,
        as_attachment=True,
        download_name=md_filename,
        mimetype="text/markdown",
    )


if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
