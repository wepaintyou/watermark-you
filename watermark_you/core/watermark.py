import os
from typing import Tuple
from PIL import Image

from watermark_you.utils import ROOT_DIR

DEFAULT_WATERMARK_IMAGE_PATH = os.path.join(
    ROOT_DIR, "data/images/default_watermark.png"
)
DEFAULT_TEST_IMAGE_PATH = os.path.join(ROOT_DIR, "data/images/default_test_image.png")


def watermark_with_transparency(
    input_image_path: str,
    output_image_path: str,
    watermark_image_path: str,
    position: Tuple[int, int],
):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    watermark = watermark.resize(base_image.size)
    width, height = base_image.size

    transparent = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.convert("RGB").save(output_image_path)


if __name__ == "__main__":

    watermark_with_transparency(
        input_image_path=DEFAULT_TEST_IMAGE_PATH,
        output_image_path="image.png",
        watermark_image_path=DEFAULT_WATERMARK_IMAGE_PATH,
        position=(150, 150),
    )
