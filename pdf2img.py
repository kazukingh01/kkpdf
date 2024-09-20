import fitz, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", required=True)
args   = parser.parse_args()

doc = fitz.open(args.path)

for i_page, page in enumerate(doc):
    print(f"load page: {i_page}")
    pix = page.get_pixmap(dpi=150)
    pix.pil_save(f"{args.path}.{i_page}.png")

