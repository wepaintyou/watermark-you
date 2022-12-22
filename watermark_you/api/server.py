from typing import Optional
from fastapi import FastAPI, UploadFile, status
from fastapi.responses import Response
from watermark_you.core.watermark import watermark_with_transparency
from PIL import Image
from watermark_you.utils import DEFAULT_WATERMARK_IMAGE_PATH

app = FastAPI()


@app.get("/")
def api_info():
    """
    The root route which returns a JSON response.
    The JSON response is delivered as:
    {
      'message': 'Watermark API!'
    }
    """
    return {"message": "Watermark API!"}


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def perform_healthcheck():
    """
    Simple route to healthcheck on.
    It basically sends a GET request to the route & hopes to get a "200"
    response code.
    Additionally, it also returns a JSON response in the form of:
    {
      'healtcheck': 'Everything OK!'
    }
    """
    return {"healthcheck": "Everything OK!"}


@app.post("/watermark", status_code=status.HTTP_200_OK)
def perform_watermark(
    image: UploadFile, watermark_image: Optional[UploadFile] = None
) -> dict[str, list]:
    """
    Apply watermark on an image.
    The final image with the added watermark will be returned.
    :param image: The image to be watermarked.
    :param watermark_image: The watermark image to be applied.
    :return: The final image with the added watermark
    """

    if watermark_image is None:
        watermark_image = Image.open(DEFAULT_WATERMARK_IMAGE_PATH)
    else:
        watermark_image = Image.open(watermark_image.file)

    watermarked_image = watermark_with_transparency(
        base_image=Image.open(image.file), watermark_image=watermark_image
    )

    return Response(content=watermarked_image.tobytes(), media_type="image/png")
