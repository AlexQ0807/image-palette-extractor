import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='image-palette-extractor',
    version='0.0.1',
    author='Alex Q',
    author_email='alex.quan0807@gmail.com',
    description='Image Color Palette Extractor Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['palette'],
    install_requires=[
        "requests", "Pillow", "extcolors"
    ],
)