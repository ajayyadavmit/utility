import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_path, output_folder=None, dpi=200):
    """
    Convert PDF to images using PyMuPDF - No external dependencies needed
    """
    if output_folder is None:
        output_folder = os.path.splitext(pdf_path)[0] + "_images"
    
    os.makedirs(output_folder, exist_ok=True)
    
    pdf_document = fitz.open(pdf_path)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        
        image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        pix.save(image_path)
        print(f"Saved page {page_num + 1} to {image_path}")
    
    pdf_document.close()
    print(f"✅ Conversion complete! Saved to: {output_folder}")

# Usage
pdf_to_images("output.pdf")