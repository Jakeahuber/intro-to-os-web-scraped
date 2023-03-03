import os
import pdfkit
from bing_image_urls import bing_image_urls
from html_templates import get_start_html, get_end_html, get_term_def_image_div

class CreatePdf:
    html_save_path = "temp.html"
    document_save_path = ""
    pdf_save_path = ""
    path_to_wkhtmltopdf = ""

    def __init__(self, document_save_path, pdf_save_path, path_to_wkhtmltopdf):
        self.document_save_path = document_save_path
        self.pdf_save_path = pdf_save_path
        self.path_to_wkhtmltopdf = path_to_wkhtmltopdf
        self.__create_pdf()

    def __create_pdf(self):
        html_file = open(self.html_save_path, 'a')
        html_file.write(get_start_html())

        document = open(self.document_save_path, "r", encoding="utf-8")
        terms_defs_images = self.__get_terms_defs_images(document)

        prev_term = ""
        for term_def_image in sorted(terms_defs_images):
            term = term_def_image[0]
            definition = term_def_image[1][0]
            image_link = term_def_image[1][1]
            if prev_term == term: # don't include duplicate definitions
                continue
            html_file.write(get_term_def_image_div(term, definition, image_link))
            prev_term = term

        html_file.write(get_end_html())
        html_file.close()
        self.__save_pdf()
        os.remove(self.html_save_path) # delete the html file after we make the pdf

    def __save_pdf(self):
        config = pdfkit.configuration(wkhtmltopdf=self.path_to_wkhtmltopdf)
        pdfkit.from_file(self.html_save_path, output_path=self.pdf_save_path, configuration=config)

    def __get_terms_defs_images(self, document):
        terms_defs_images = []  # (term, (def, image))
        for paragraph in document:
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
        urls = bing_image_urls(query, limit=1)
        if (len(urls) > 0):
            return urls[0]
        # couldn't find an image. Display this image.
        return "https://filestore.community.support.microsoft.com/api/images/ext?url=https%3A%2F%2Fanswerscdn.microsoft.com%2Fstatic%2Fimages%2Fimage-not-found.jpg"