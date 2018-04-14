from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
# print("wordFile:",wordFile)
document = ZipFile(wordFile)
# print("document:",document)
xml_content = document.read('word/document.xml')
# print("xml_content:",xml_content)
wordObj = BeautifulSoup(xml_content.decode('utf-8'), "lxml-xml")
print("wordObj:",wordObj)
textStrings = wordObj.findAll("w:t")
print("textStrings:",textStrings)
for textElem in textStrings:
    closeTag = ""
    try:
        style = textElem.parent.previousSibling.find("w:pStyle")
        if style is not None and style["w:val"] == "Title":
            print("<h1>")
            closeTag = "</h1>"
    except AttributeError: #不打印标签
        pass
    print(textElem.text)
    print(closeTag)