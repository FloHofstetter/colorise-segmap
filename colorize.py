from Colorize.colorize import Colorizer
from PIL import Image
import argparse
import os


def setup_parser() -> argparse.Namespace:
    """
    Ask user for source and destination path.

    :return: Arguments from CLI user.
    """
    parser: argparse.ArgumentParser
    parser = argparse.ArgumentParser(description="Colorize segmentation mask Images.")
    parser.add_argument(
        "src",
        metavar="src",
        type=str,
        help="Source path of segmentation mask",
    )
    parser.add_argument(
        "dst",
        metavar="dst",
        type=str,
        help="Destination path of colorized picture",
    )
    args: argparse.Namespace = parser.parse_args()

    return args


def main() -> None:
    args: argparse.Namespace
    args = setup_parser()

    img: Image.Image = Image.open(args.src)
    colorizer: Colorizer = Colorizer()
    img_seg: Image.Image
    img_seg = colorizer.colorize(img)
    img_seg.save(args.dst)


if __name__ == "__main__":
    main()
