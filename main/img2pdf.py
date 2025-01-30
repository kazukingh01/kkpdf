import argparse
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True)
    args = parser.parse_args()
    img = Image.open(args.path)
    img_width, img_height = img.size
    page_width, page_height = letter
    scale = min(page_width / img_width, page_height / img_height)
    new_width = img_width * scale
    new_height = img_height * scale
    c = canvas.Canvas(f"{args.path}.pdf", pagesize=letter)
    c.setFillColorRGB(1, 1, 1)
    c.rect(0, 0, page_width, page_height, fill=1, stroke=0)
    x = (page_width - new_width) / 2
    y = (page_height - new_height) / 2
    c.drawImage(
        ImageReader(img),
        x,
        y,
        width=new_width,
        height=new_height,
        preserveAspectRatio=True,
        mask='auto'
    )
    c.showPage()
    c.save()
