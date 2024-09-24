import easyocr
reader = easyocr.Reader(['ru','ru'])
result = reader.readtext('bw.jpg')