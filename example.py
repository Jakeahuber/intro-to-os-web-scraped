from create_document import CreateDocument
from create_pdf import CreatePdf

document_save_path = "v2_intro_to_os_web_scraped.txt"
pdf_save_path = "v2_intro_to_os_web_scraped.pdf"
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

#CreateDocument(document_save_path)
CreatePdf(document_save_path, pdf_save_path, path_to_wkhtmltopdf)