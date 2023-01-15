import traceback
from palette.extractor import PaletteExtractor

try:
    image_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/a/ad/Claude_Monet_-_Water_Lilies_and_Japanese_Bridge.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/31/Michael_Jackson_in_1988.jpg"
    ]
    html = PaletteExtractor.build_html_palette_preview(image_urls=image_urls, to_hex=True)
    print(html)
except Exception as e:
    print(e)
    traceback.print_exc()