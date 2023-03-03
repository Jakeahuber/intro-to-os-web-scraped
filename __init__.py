from create_document import CreateDocument
from create_pdf import CreatePdf

#CreateDocument("intro_to_os_web_scraped.txt")
CreatePdf("intro_to_os_web_scraped.pdf", r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe', "intro_to_os_web_scraped.txt")