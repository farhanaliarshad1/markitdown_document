# Document to Markdown Converter

A lightweight Flask web app that converts documents into clean Markdown — so you can paste them into Claude, ChatGPT, or any LLM and use as few tokens as possible.

Raw files like PDFs or Word docs are token-heavy when fed directly to an LLM. Converting them to Markdown first gives you the same content in a leaner, structured format that models read well.

## How it works

1. Open the app in your browser
2. Upload any supported file
3. Get a `.md` file back — ready to copy into any LLM

Conversion is done entirely by the [MarkItDown](https://github.com/microsoft/markitdown) Python library. No external APIs, no LLM calls, no cost.

## Supported formats

| Category | Formats |
|---|---|
| Documents | PDF, Word (.docx), Excel (.xlsx), PowerPoint (.pptx) |
| Images | JPG, PNG, GIF, BMP, TIFF, WEBP |
| Audio | MP3, WAV, M4A, OGG, FLAC |
| Web & Data | HTML, CSV, JSON, XML |
| Other | ZIP, EPUB |

## Getting started

```bash
pip install flask "markitdown[all]"
python app.py
```

Then visit `http://localhost:5000`.

> Max file size: 50 MB
