import pytesseract
from PIL import Image
def ocr_image(img_path):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img)
    return text

