import pytesseract

def perform_ocr(preprocessed_image, language='mar'):  #'mar' stands for marwadi not march, since it's my local language
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(
        preprocessed_image,
        lang=language,
        config=custom_config
    )
    return text
