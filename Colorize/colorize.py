import numpy as np
from PIL import Image

COLORMAP = np.array(
    [
        (230, 25, 75),
        (60, 180, 75),
        (255, 225, 25),
        (67, 99, 216),
        (245, 130, 49),
        (145, 30, 180),
        (70, 240, 240),
        (240, 50, 230),
        (188, 246, 12),
        (250, 190, 190),
        (0, 128, 128),
        (230, 190, 255),
        (154, 99, 36),
        (255, 250, 200),
        (128, 0, 0),
        (170, 255, 195),
        (128, 128, 0),
        (255, 216, 177),
        (0, 0, 117),
        (128, 128, 128),
        (255, 255, 255),
        (0, 0, 0),
    ],
    dtype="uint8",
)


class Colorizer(object):
    def __init__(self, colormap: np.ndarray = COLORMAP) -> None:
        if not isinstance(colormap, np.ndarray):
            raise TypeError(
                f"Expected colormap to be of type numpy.ndarray, got {type(colormap)}."
            )
        if colormap.dtype != "uint8":
            raise TypeError(
                f'Expected colormap to be of dtype="uint8", got {colormap.dtype}.'
            )

        self.colormap: np.ndarray = colormap

    def colorize(self, image: Image.Image) -> Image.Image:
        """
        Colorize given segmentation mask.

        :param image: Segmentation mask as PIL image.
        :return: Colorized PIL image.
        """
        if not isinstance(image, Image.Image):
            raise TypeError(
                f"Expected colormap to be of type PIL.Image.Image, got {type(image)}."
            )

        image_a: np.ndarray
        image_a = np.asarray(image)
        image_a = np.repeat(np.expand_dims(image_a, axis=0), 3, axis=0)
        image_a = image_a.transpose(1, 2, 0)

        seg_class: int
        color: np.ndarray
        for seg_class, color in enumerate(self.colormap):
            seg_class_a: np.ndarray
            seg_class_a = np.array(seg_class)
            image_a = np.where(image_a == seg_class_a, color, image_a)

        return Image.fromarray(image_a)


def main():
    pass


if __name__ == "__main__":
    main()
