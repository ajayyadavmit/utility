# Utility

1. converting between images to PDF files.
2. COnverting pdf to image file. 

## Contents

- [jpg2pdf/img2pdf.py](jpg2pdf/img2pdf.py) — converts JPG/JPEG images in a folder into a single PDF
- [pdf2jpg/pdf2img.py](pdf2jpg/pdf2img.py) — converts each page of a PDF into PNG image files

---

## 1) JPG/JPEG to PDF

File: [jpg2pdf/img2pdf.py](jpg2pdf/img2pdf.py)

This script defines `combine_images_to_pdf_pillow(image_folder, output_pdf, dpi=150)` and uses Pillow to combine all JPG/JPEG files from a folder into one PDF.

### Behavior

- Searches the target folder for files matching:
  - `*.jpg`
  - `*.jpeg`
  - `*.JPG`
  - `*.JPEG`
- Sorts the files alphabetically before processing
- Converts images to `RGB` when needed
- Handles transparent or palette-based images by creating a white background first
- Saves the result as a single multipage PDF

### Example

```python
from jpg2pdf.img2pdf import combine_images_to_pdf_pillow

combine_images_to_pdf_pillow("images", "output.pdf", dpi=150)
```

When run directly, the script currently uses:

```python
combine_images_to_pdf_pillow("images", "output.pdf")
```

Update the folder and output names to match your project before running it.

---

## 2) PDF to Images

File: [pdf2jpg/pdf2img.py](pdf2jpg/pdf2img.py)

This script defines `pdf_to_images(pdf_path, output_folder=None, dpi=200)` and uses PyMuPDF (`fitz`) to render each PDF page to a PNG file.

### Behavior

- Opens the PDF using `fitz.open(...)`
- Creates the output folder if it does not already exist
- Renders each page at a DPI-based zoom factor
- Saves pages as:
  - `page_1.png`
  - `page_2.png`
  - etc.
- Defaults the output folder to `<pdf_name>_images` when no folder is supplied

### Example

```python
from pdf2jpg.pdf2img import pdf_to_images

pdf_to_images("output.pdf", output_folder="pdf_pages", dpi=200)
```

When run directly, the script currently calls:

```python
pdf_to_images("output.pdf")
```

This creates a folder named `output_images` by default (derived from the PDF filename).

---

## Dependencies

Install the required libraries:

```bash
pip install pillow PyMuPDF
```

---

## Notes

- The scripts are simple utility functions rather than full command-line tools.
- They include example calls in the `if __name__ == "__main__":` sections, but you should edit those paths to match your actual files.
- The project is intended for basic local conversions and is not a packaged app with a formal CLI.
