import os
from typing import Optional, Tuple
from PIL import Image

from watermark_you.utils import (
    DEFAULT_WATERMARK_IMAGE_PATH,
    DEFAULT_TEST_IMAGE_PATH,
)


def watermark_with_transparency(
    base_image: Image,
    watermark_image: Image,
    output_image_path: Optional[str] = None,
    position: Optional[Tuple[int, int]] = (150, 150),
):
    watermark_image = watermark_image.resize(base_image.size)
    width, height = base_image.size

    final_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    final_image.paste(base_image, (0, 0))
    final_image.paste(watermark_image, position, mask=watermark_image)
    final_image = final_image.convert("RGB")
    if output_image_path is not None:
        final_image.save(output_image_path)

    return final_image


if __name__ == "__main__":

    watermark_with_transparency(
        base_image=Image.open(DEFAULT_TEST_IMAGE_PATH),
        watermark_image=Image.open(DEFAULT_WATERMARK_IMAGE_PATH),
        output_image_path="image.png",
        position=(150, 150),
    )
