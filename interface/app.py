import streamlit as st
from watermark_you.utils import ROOT_DIR, DEFAULT_WATERMARK_IMAGE_PATH
from watermark_you.core.watermark import watermark_with_transparency
from interface.utils import images_to_zip
from itertools import cycle
from PIL import Image
import os

icon_path = os.path.join(ROOT_DIR, "data/images/wepaintyou_logo_no_background.png")
title_path = os.path.join(ROOT_DIR, "data/images/watermark_you.png")

st.set_page_config(
    page_title="Watermark You",
    page_icon=icon_path,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.image(title_path)

images = st.file_uploader("Choose images to apply watermark to", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

if images is not None and len(images) != 0:
    
    if not isinstance(images, list):
        images = [images]
        
    with st.expander("Show loaded images", False):
        cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
        for idx, image in enumerate(images):
            next(cols).image(image, width=250)
    
    watermark_image = st.file_uploader
    
    if st.button("Apply watermark"):
        st.session_state["watermarked_images"] = []
        for image in images:
            st.session_state["watermarked_images"].append(watermark_with_transparency(
                base_image=Image.open(image),
                watermark_image=Image.open(DEFAULT_WATERMARK_IMAGE_PATH)
            ))
    
    if "watermarked_images" in st.session_state:
        with st.expander("Show watermarked images", False):
            cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
            for idx, image in enumerate(st.session_state["watermarked_images"]):
                next(cols).image(image, width=250)
        
        zip_images_file = images_to_zip(st.session_state["watermarked_images"])
        
        st.download_button(
            label="Download",
            data=zip_images_file,
            file_name="watermarked_images.zip"
        )