## Image Palette Extractor Package for Python (Private)
<hr>

### Setup
```
pip install git+https://github.com/AlexQ0807/image-palette-extractor.git
```


### Example

```
from palette.extractor import PaletteExtractor
from pprint import pprint

img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
palette = PaletteExtractor.extract_palette_from_url_image(img_url, to_hex=True)

pprint(palette)
```

```
{'palette': [{'color': '#5a779f', 'pixels': 549515},
             {'color': '#121615', 'pixels': 363708},
             {'color': '#91a197', 'pixels': 120572},
             {'color': '#1e2d66', 'pixels': 73002},
             {'color': '#c1c27c', 'pixels': 24165},
             {'color': '#5e6924', 'pixels': 6796},
             {'color': '#bda720', 'pixels': 1328},
             {'color': '#252995', 'pixels': 465},
             {'color': '#5b2f00', 'pixels': 240},
             {'color': '#f2ffff', 'pixels': 183},
             {'color': '#6986ea', 'pixels': 15},
             {'color': '#b3cafe', 'pixels': 4},
             {'color': '#b97b42', 'pixels': 4},
             {'color': '#295846', 'pixels': 2},
             {'color': '#7b595a', 'pixels': 1}],
 'total_pixels': 1140000}

```