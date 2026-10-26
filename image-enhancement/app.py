
import io
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

st.set_page_config(
    page_title="Image Enhancement Studio",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Image Enhancement Studio")
st.write("Upload an image and improve its quality using different tools.")

uploaded_file = st.file_uploader(
    "Upload your image",
    type=["png", "jpg", "jpeg", "webp", "bmp"]
)

if uploaded_file is not None:
    try:
        original = Image.open(uploaded_file)
        original = ImageOps.exif_transpose(original)

        if original.mode not in ("RGB", "RGBA"):
            original = original.convert("RGB")

        st.sidebar.header("Enhancement Settings")

        brightness = st.sidebar.slider(
            "Brightness", 0.1, 3.0, 1.0, 0.1
        )
        contrast = st.sidebar.slider(
            "Contrast", 0.1, 3.0, 1.0, 0.1
        )
        sharpness = st.sidebar.slider(
            "Sharpness", 0.0, 3.0, 1.0, 0.1
        )
        saturation = st.sidebar.slider(
            "Color Saturation", 0.0, 3.0, 1.0, 0.1
        )

        effect = st.sidebar.selectbox(
            "Choose a Filter",
            [
                "None",
                "Grayscale",
                "Sepia",
                "Blur",
                "Smooth",
                "Detail",
                "Edge Enhance"
            ]
        )

        rotation = st.sidebar.selectbox(
            "Rotate Image",
            [0, 90, 180, 270]
        )

        resize_width = st.sidebar.number_input(
            "Resize Width (0 = original size)",
            min_value=0,
            max_value=10000,
            value=0,
            step=10
        )

        # Apply enhancements
        enhanced = ImageEnhance.Brightness(
            original
        ).enhance(brightness)

        enhanced = ImageEnhance.Contrast(
            enhanced
        ).enhance(contrast)

        enhanced = ImageEnhance.Sharpness(
            enhanced
        ).enhance(sharpness)

        enhanced = ImageEnhance.Color(
            enhanced
        ).enhance(saturation)

        # Apply selected filter
        if effect == "Grayscale":
            enhanced = ImageOps.grayscale(
                enhanced
            ).convert("RGB")

        elif effect == "Sepia":
            gray = ImageOps.grayscale(enhanced)
            enhanced = ImageOps.colorize(
                gray,
                black="#24160f",
                white="#f4d7a1"
            )

        elif effect == "Blur":
            enhanced = enhanced.filter(
                ImageFilter.GaussianBlur(radius=2)
            )

        elif effect == "Smooth":
            enhanced = enhanced.filter(ImageFilter.SMOOTH)

        elif effect == "Detail":
            enhanced = enhanced.filter(ImageFilter.DETAIL)

        elif effect == "Edge Enhance":
            enhanced = enhanced.filter(
                ImageFilter.EDGE_ENHANCE
            )

        # Rotate image
        if rotation:
            enhanced = enhanced.rotate(
                rotation,
                expand=True
            )

        # Resize image while preserving aspect ratio
        if resize_width > 0 and enhanced.width > resize_width:
            new_height = round(
                enhanced.height * resize_width / enhanced.width
            )
            enhanced = enhanced.resize(
                (resize_width, new_height),
                Image.Resampling.LANCZOS
            )

        # Display original and enhanced images
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(original, width="stretch")
            st.caption(
                f"Dimensions: {original.width} × {original.height}"
            )

        with col2:
            st.subheader("Enhanced Image")
            st.image(enhanced, width="stretch")
            st.caption(
                f"Dimensions: {enhanced.width} × {enhanced.height}"
            )

        # Download options
        output_format = st.selectbox(
            "Download Format",
            ["PNG", "JPEG"]
        )

        buffer = io.BytesIO()

        if output_format == "JPEG":
            enhanced.convert("RGB").save(
                buffer,
                format="JPEG",
                quality=95
            )
            mime_type = "image/jpeg"
            extension = "jpg"
        else:
            enhanced.save(buffer, format="PNG")
            mime_type = "image/png"
            extension = "png"

        st.download_button(
            label="Download Enhanced Image",
            data=buffer.getvalue(),
            file_name=f"enhanced_image.{extension}",
            mime=mime_type,
            type="primary"
        )

    except Exception as error:
        st.error(f"Unable to process image: {error}")

else:
    st.info("Please upload an image to get started.")
