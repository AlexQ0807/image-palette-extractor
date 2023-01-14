import extcolors
import requests
from PIL import Image
import io
from pprint import pprint

class PaletteExtractor:
    # https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
    image_formats = ["image/png", "image/jpeg", "image/jpg", "image/svg+xml", "image/webp", ""]

    @classmethod
    def convert_rgb_to_hex(cls, rgb):
        try:
            return '#%02x%02x%02x' % rgb
        except Exception as e:
            raise e

    @classmethod
    def is_valid_image_url(cls, img_url: str):
        try:
            r = requests.head(img_url)
            if r.headers["content-type"] in cls.image_formats:
                return True
            return False
        except Exception as e:
            raise e

    @classmethod
    def extract_palette(cls, img: Image, to_hex: bool):
        try:
            color_palette, num_pixels = extcolors.extract_from_image(img)

            if to_hex:
                color_palette = [
                    {"color": cls.convert_rgb_to_hex(color_data[0]), "pixels": color_data[1]}
                    for color_data in color_palette
                ]
            else:
                color_palette = [
                    {"color": color_data[0], "pixels": color_data[1]}
                    for color_data in color_palette
                ]

            return {
                "palette": color_palette,
                "total_pixels": num_pixels
            }
        except Exception as e:
            raise e

    @classmethod
    def extract_palette_from_url_image(cls, img_url: str, to_hex: bool = False):
        try:
            if cls.is_valid_image_url(img_url):
                response = requests.get(img_url, stream=True)
                img_byte = response.content
                img = Image.open(io.BytesIO(img_byte))
                return cls.extract_palette(img=img, to_hex=to_hex)
        except Exception as e:
            raise e

from pprint import pprint

img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"

# Fetch remaining credits
palette = PaletteExtractor.extract_palette_from_url_image(img_url, to_hex=True)
pprint(palette)