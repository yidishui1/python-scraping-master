from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    #Set a threshold value for the image, and save
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)

    #call tesseract to do OCR on the newly created image
    subprocess.call(["tesseract", newFilePath, "./files/output"])
    
    #Open and read the resulting data file
    outputFile = open("./files/output.txt", 'r')
    print(outputFile.read())
    outputFile.close()

cleanFile("./files/text_2.png", "./files/text_2_clean.png")