from zipfile import ZipFile
from PIL import Image
import io
import streamlit as st

@st.experimental_memo
def images_to_zip(images: list):
    """ Converts PIL image objects into BytesIO in-memory bytes buffers."""

    copied_images = images.copy()

    for i, pil_image in enumerate(copied_images):
        file_object = io.BytesIO()
        pil_image.save(file_object, "PNG")
        copied_images[i] = file_object  # Replace PIL image object with BytesIO memory buffer.

    # Create an in-memory zip file from the in-memory image file data.
    zip_file_bytes_io = io.BytesIO()

    with ZipFile(zip_file_bytes_io, 'w') as zip_file:
        for i, bytes_stream in enumerate(copied_images):
            zip_file.writestr(f"{i+1}.png", bytes_stream.getvalue())
            
    return zip_file_bytes_io