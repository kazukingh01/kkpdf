from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# 画像ファイルのパス
png_path = "../10-07.png"
# 生成するPDFファイルのパス
pdf_path = "../10-07.pdf"

# 画像を開きます
img = Image.open(png_path)

# 画像をリサイズします。このステップは必要に応じてスキップしても構いません。
# PDFのサイズ (ここではUS Letterサイズ) に合わせて画像をリサイズします。

# ReportLabのキャンバスを作成します
c = canvas.Canvas(pdf_path)

# PIL画像をReportLabが使用できる画像に変換します
img = ImageReader(img)

# 画像をPDFに描画します
c.drawImage(img, 0, 0, *letter)

# PDFを保存します
c.save()
