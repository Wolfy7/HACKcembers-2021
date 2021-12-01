"""
https://www.floriandalwigk.de/santas-geschenk-hackcember-1
"""

import zipfile
import os

with zipfile.ZipFile('geschenk.zip', 'r') as zf:
    file = zf.namelist()[0]
    zf.extractall()
    while ".zip" in file:
        with zipfile.ZipFile(file, 'r') as zipf:
            file = zipf.namelist()[0]
            zipf.extractall()

for file in os.listdir():
    if file.endswith(".zip") and file != "geschenk.zip":
        os.remove(file)