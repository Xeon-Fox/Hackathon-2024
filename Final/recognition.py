import easyocr


def recognize_text(image_path):
       reader = easyocr.Reader(['ru', 'ru'], gpu=False)  
       result = reader.readtext(image_path, detail=0)
       return " ".join(result)