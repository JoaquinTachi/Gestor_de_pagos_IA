print("proyecto iniciado...")

from pathlib import Path
from PIL import Image
import pytesseract

ruta_comprobante = Path("comprobantes/comprobante1.jpg")

with Image.open(ruta_comprobante) as imagen:
    texto= pytesseract.image_to_string(imagen)
    print(texto)

