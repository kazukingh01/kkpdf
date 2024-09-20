import fitz, argparse, os


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path",    type=str, required=True)
    parser.add_argument("--outdir",  type=str, default="./output/")
    parser.add_argument("--outname", type=str)
    parser.add_argument("--dpi",     type=int, default=150)
    args = parser.parse_args()
    doc  = fitz.open(args.path)
    if args.outname is None:
        args.outname = os.path.basename(args.path)
    os.makedirs(args.outdir, exist_ok=True)
    for i_page, page in enumerate(doc):
        print(f"load page: {i_page}")
        pix = page.get_pixmap(dpi=args.dpi)
        pix.pil_save(f"{args.outdir}/{args.outname}.{i_page}.png")

