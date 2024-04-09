from PIL import Image
import pytesseract
import os

#defining the location of tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#empty list for names
isimliste = []

#function for parsing names from image
def isimoku(text):
    lines = [line.strip() for line in text.split('\n') if line.strip() != '']
    name_line_index = lines.index('Sayin') + 1 if 'Sayin' in lines else None
    return lines[name_line_index] if name_line_index and name_line_index < len(lines) else None

#main loop
for y in range(118,352):

    #load the image from file
    image_path = f'C:/Users/Xigmatek-1/Desktop/mail/sertifikalar/{y}.png'
    image = Image.open(image_path)

    #use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    #replacing i's with to prevent bugs
    isim = isimoku(text).replace("i","I") + ".png"
    
    #renaming code
    try:
        os.rename(f"{y}.png",isim)
        isim = ''
        text = ''
    except:
        #for imageses that couldn't be renamed
        print(f"belge {y} atlandi")
