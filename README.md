# PDF to Markdown Converter

A simple web app that converts PDF files into clean Markdown — built so you can feed documents to any LLM (Claude, ChatGPT, or any other) using far fewer tokens than pasting raw PDF text.

## Why

PDFs are token-heavy when dumped as plain text. Converting to Markdown first strips the noise and gives you structured, compact content that LLMs handle well.

## How it works

Upload a PDF through the browser, and it comes back as a `.md` file — ready to paste into Claude, ChatGPT, or whichever model you're using. Conversion is handled entirely by the [`markitdown`](https://github.com/microsoft/markitdown) Python library. No external APIs, no LLM calls, no cost.

## Usage

```bash
pip install flask markitdown
python app.py
```

Then open `http://localhost:5000`, upload a PDF, and download the Markdown.

## Supported formats

PDF, Word, Excel, PowerPoint, Images, Audio, HTML, CSV, JSON, XML, ZIP, EPUB — anything [MarkItDown](https://github.com/microsoft/markitdown) handles.

## Limits

- Up to 50 MB per file
