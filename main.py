from pathlib import Path

from PIL import Image
import pytesseract


def extraer_texto(ruta_imagen: Path) -> str:
    with Image.open(ruta_imagen) as imagen:
        return pytesseract.image_to_string(imagen)


def main() -> None:
    print("proyecto iniciado...")

    ruta_comprobante = Path("comprobante/comprobante1.jpg")
    texto = extraer_texto(ruta_comprobante)
    print(texto)


if __name__ == "__main__":
    main()

