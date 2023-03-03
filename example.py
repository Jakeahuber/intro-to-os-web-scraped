from create_document import CreateDocument
from create_pdf import CreatePdf

document_name = "intro_to_os_web_scraped.txt"
pdf_name = "intro_to_os_web_scraped.pdf"
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

CreateDocument(document_name)
CreatePdf(document_name, pdf_name, path_to_wkhtmltopdf)