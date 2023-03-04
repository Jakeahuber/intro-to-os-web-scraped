import os
import pdfkit
from bing_image_urls import bing_image_urls
from html_templates import get_start_html, get_end_html, get_term_def_image_div, add_to_table_of_contents
from term_def_image import TermDefImage

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

        self.__write_html_table_of_contents(terms_defs_images, html_file)
        self.__write_html_terms_defs_images(terms_defs_images, html_file)

        html_file.write(get_end_html())
        html_file.close()
        self.__save_pdf()
        #os.remove(self.html_save_path) # delete the html file after we make the pdf

    # writes the table of contents to the html file
    def __write_html_table_of_contents(self, terms_defs_images, html_file):
        prev_term = ""
        for term_def_image in terms_defs_images:
            term = term_def_image.term
            if prev_term == term: # don't include duplicate definitions
                continue
            html_file.write(add_to_table_of_contents(term))
            prev_term = term

    # writes each term with its corresponding definition and image to the html file
    def __write_html_terms_defs_images(self, terms_defs_images, html_file):
        prev_term = ""
        for term_def_image in terms_defs_images:
            term = term_def_image.term
            definition = term_def_image.definition
            image_link = term_def_image.image_link
            if prev_term == term: # don't include duplicate definitions
                continue
            html_file.write(get_term_def_image_div(term, definition, image_link))
            prev_term = term

    # saves a pdf containing the contents of the html_save_path file
    def __save_pdf(self):
        config = pdfkit.configuration(wkhtmltopdf=self.path_to_wkhtmltopdf)
        pdfkit.from_file(self.html_save_path, output_path=self.pdf_save_path, configuration=config)

    # returns a list of TermDefImage objects for each term in the document
    def __get_terms_defs_images(self, document):
        terms_defs_images = []  # (term, (def, image))
        for paragraph in document:
            # don't include empty lines
            if (len(paragraph.split(":", 1)) == 1):
                continue
            paragraph = paragraph.encode('latin-1', 'replace').decode('latin-1') # some characters without this line cannot be encoded
            
            # Each term and definition is of the following format in the txt file:
            # 'Single-board_computer : A single-board computer (SBC) is a ...'
            term = paragraph.split(" : ", 1)[0].replace("_", " ")
            definition = paragraph.split(" : ", 1)[1] 
            first_image_link = self.__get_first_image_link(term)

            term_def_image = TermDefImage(term, definition, first_image_link)
            terms_defs_images.append(term_def_image)
        
        return self.__sorted_copy(terms_defs_images)
    
    # returns a sorted copy of the terms_defs_images object
    def __sorted_copy(self, terms_defs_images):
        return sorted(terms_defs_images, key=lambda x: x.term)

    # Given a query, returns the first image Bing finds for the image.
    # Bing was chosen for this task because of its library's simplicity
    def __get_first_image_link(self, query):
        urls = bing_image_urls(query, limit=1)
        if (len(urls) > 0):
            return urls[0]
        # couldn't find an image. Display a default image (says 'not found').
        return "https://filestore.community.support.microsoft.com/api/images/ext?url=https%3A%2F%2Fanswerscdn.microsoft.com%2Fstatic%2Fimages%2Fimage-not-found.jpg"