import os
import sys

from PIL import Image, ExifTags


SUPPORTED_FORMATS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".tiff",
    ".tif",
    ".webp",
    ".bmp",
}


def format_file_size(size):
    if size < 1024:
        return f"{size} B"

    if size < 1024 ** 2:
        return f"{size / 1024:.2f} KB"

    if size < 1024 ** 3:
        return f"{size / (1024 ** 2):.2f} MB"

    return f"{size / (1024 ** 3):.2f} GB"


def get_exif_data(image):
    exif_data = {}

    try:
        exif = image.getexif()

        for tag_id, value in exif.items():
            tag_name = ExifTags.TAGS.get(tag_id, tag_id)
            exif_data[tag_name] = str(value)

    except Exception:
        pass

    return exif_data


def analyze_image(image_path):
    if not os.path.isfile(image_path):
        print("Error: File does not exist.")
        return None

    extension = os.path.splitext(image_path)[1].lower()

    if extension not in SUPPORTED_FORMATS:
        print("Error: Unsupported image format.")
        return None

    try:
        with Image.open(image_path) as image:

            width, height = image.size
            exif_data = get_exif_data(image)

            metadata = {
                "type": "image",
                "file_name": os.path.basename(image_path),
                "file_size": format_file_size(os.path.getsize(image_path)),
                "format": image.format,
                "width": width,
                "height": height,
                "resolution": f"{width} x {height}",
                "color_mode": image.mode,
                "exif": exif_data,
            }

            print("\n================================")
            print("IMAGE METADATA REPORT")
            print("================================")

            print(f"\nFile Name       : {metadata['file_name']}")
            print(f"File Size       : {metadata['file_size']}")
            print(f"Format          : {metadata['format']}")

            print("\nIMAGE")
            print("--------------------------------")
            print(f"Width           : {width}")
            print(f"Height          : {height}")
            print(f"Resolution      : {metadata['resolution']}")
            print(f"Color Mode      : {image.mode}")

            print("\nMETADATA")
            print("--------------------------------")

            if exif_data:
                for key, value in exif_data.items():
                    print(f"{key:<20}: {value}")
            else:
                print("No EXIF metadata found.")

            return metadata

    except Exception as error:
        print(f"Error analyzing image: {error}")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_analyzer.py <image_path>")
        sys.exit(1)

    analyze_image(sys.argv[1])