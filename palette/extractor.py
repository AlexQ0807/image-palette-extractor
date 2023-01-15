import extcolors
import requests
from PIL import Image
from bs4 import BeautifulSoup
import io
from pprint import pprint

class PaletteExtractor:
    # https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
    image_formats = ["image/png", "image/jpeg", "image/jpg", "image/svg+xml", "image/webp", ""]
    preview_height = 40
    preview_width = 50

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
                    {"color": cls.convert_rgb_to_hex(color_data[0]).upper(), "pixels": color_data[1]}
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
            return None
        except Exception as e:
            raise e

    @classmethod
    def build_html_palette_preview(cls, image_urls: list[str], to_hex=False):
        try:
            html = '<table border="1">'
            html += '<tr><td>Image</td><td>Palette</td></tr>'

            for image_url in image_urls:
                palette_data: dict = cls.extract_palette_from_url_image(img_url=image_url, to_hex=to_hex)

                if palette_data is not None:

                    palette = palette_data['palette']
                    total_pixels = palette_data['total_pixels']

                    # Image Row - START
                    html += "<tr>"
                    html += '''
                        <td style="text-align: center;">
                            <img style="max-width: 400px; max-height: 600px;" src="{0}" alt="{0}" />
                        </td>
                    '''.format(image_url)

                    html += "<td>"
                    html += '<div style="display: grid; grid-template-columns: repeat(6, 180px); justify-items: center;">'
                    for color_data in palette:
                        color_code = color_data['color']

                        if isinstance(color_code, tuple):
                            color_code = "rgb{}".format(color_code)

                        percent_composition = round((color_data['pixels'] / total_pixels) * 100, 2)
                        if percent_composition == 0:
                            percent_composition = "<{}".format(percent_composition)
                        html += '''
                        <div style="margin: 20px">
                            <div style="width: {0}px; height: {1}px;  background: {2}; border: 1px solid black;"></div>
                            <div style="display: flex; flex-direction: column;">
                                <span>{2}</span>
                                <span><b>{3}%</b></span>
                            </div>
                        </div>
                        '''.format(cls.preview_width, cls.preview_height, color_code, percent_composition)

                    html += "</div></td>"
                    html += "</tr>"
                    # Image Row - END

            html += "</table>"
            soup = BeautifulSoup(html, "html.parser")
            return soup.prettify()
        except Exception as e:
            raise e
