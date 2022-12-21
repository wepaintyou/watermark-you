from fastapi import FastAPI, status
from watermark_you.core.watermark import watermark_with_transparency

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
def perform_watermark():
    """
    Apply watermark on a series of images.
    The final images with the added watermark will be returned.
    """
    watermarked_images = []
    return {"watermarked_images": watermarked_images}
