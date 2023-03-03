import os
import pdfkit
from bing_image_urls import bing_image_urls
from html_templates import get_start_html, get_end_html, get_term_def_image_div

class CreatePdf:
    html_file_name = "temp.html"
    document_name = ""
    pdf_name = ""
    path_to_wkhtmltopdf = ""

    def __init__(self, document_name, pdf_name, path_to_wkhtmltopdf):
        self.document_name = document_name
        self.pdf_name = pdf_name
        self.path_to_wkhtmltopdf = path_to_wkhtmltopdf
        self.__create_pdf()

    def __create_pdf(self):
        html_file = open(self.html_file_name, 'a')
        html_file.write(get_start_html())

        document = open(self.document_name, "r", encoding="utf-8")
        terms_defs_images = self.__get_terms_defs_images(document)

        prev_term = ""
        for term_def_image in sorted(terms_defs_images):
            term = term_def_image[0]
            definition = term_def_image[1][0]
            image_link = term_def_image[1][1]
            if prev_term == term:
                continue
            html_file.write(get_term_def_image_div(term, definition, image_link))
            prev_term = term_def_image[0]

        html_file.write(get_end_html())
        html_file.close()
        self.__save_pdf()
        os.remove(self.html_file_name) # delete the html file after we make the pdf

    def __save_pdf(self):
        config = pdfkit.configuration(wkhtmltopdf=self.path_to_wkhtmltopdf)
        pdfkit.from_file(self.html_file_name, output_path=self.pdf_name, configuration=config)

    def __get_terms_defs_images(self, document):
        terms_defs_images = []  # (term, (def, image))
        for paragraph in document:
            # need to change encoding so FPDF can read the contents
            paragraph = paragraph.encode('latin-1', 'replace').decode('latin-1')
            # don't include empty lines
            if (len(paragraph.split(":", 1)) == 1):
                continue

            term = paragraph.split(" : ", 1)[0].replace("_", " ")
            definition = paragraph.split(" : ", 1)[1] 
            first_image_link = self.__get_first_image_link(term)
            term_def_image = (term, (definition, first_image_link))
            terms_defs_images.append(term_def_image)
        
        return terms_defs_images

    def __get_first_image_link(self, query):
        url = bing_image_urls(query, limit=1)[0]
        return url