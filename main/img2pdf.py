import argparse
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="複数の画像を1つのPDFに変換します")
    parser.add_argument("paths", type=str, nargs="+", help="変換する画像ファイルのパスを指定してください")
    parser.add_argument("--output", type=str, default="output.pdf", help="出力するPDFファイル名 (デフォルト: output.pdf)")
    args = parser.parse_args()

    page_width, page_height = letter
    c = canvas.Canvas(args.output, pagesize=letter)

    for path in args.paths:
        img = Image.open(path)
        img_width, img_height = img.size
        scale = min(page_width / img_width, page_height / img_height)
        new_width = img_width * scale
        new_height = img_height * scale
        x = (page_width - new_width) / 2
        y = (page_height - new_height) / 2
        c.setFillColorRGB(1, 1, 1)
        c.rect(0, 0, page_width, page_height, fill=1, stroke=0)
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
