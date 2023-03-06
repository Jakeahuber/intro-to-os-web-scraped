import wikipedia

class CreateDocument:
    document_save_path = ""
    character_limit = 1800 # the maximum length of a paragraph for a definition

    def __init__(self, document_save_path):
        self.document_save_path = document_save_path
        self.__create_document()

    def __create_document(self):
        operating_systems_page = wikipedia.page("Operating System", auto_suggest=False)
        links = operating_systems_page.links
        for link in links:
            self.__write_first_paragraph_to_document(link, self.document_save_path)

    # prints the first non-empty paragraph that appears in the html content provided
    def __write_first_paragraph_to_document(self, link, document_name):
        wikipedia_page_name = link

        # Don't include wikipedia related pages, such as 'Wikipedia: Citation Needed'
        if "Wikipedia" in wikipedia_page_name:
            return
        try:
            wikipedia_page_summary = wikipedia.summary(wikipedia_page_name, auto_suggest=False)
        except Exception:
            return
        first_paragraph = wikipedia_page_summary.split("\n")[0]
        first_paragraph_with_char_limit = self.get_first_paragraph_with_char_limit(first_paragraph)

        document = open(document_name, 'a', encoding="utf-8")
        document.write(f"{wikipedia_page_name} : {first_paragraph_with_char_limit} \n\n")
        document.close()

    # shortens the paragraph if it exceeds the character limit
    def get_first_paragraph_with_char_limit(self, paragraph):
        if len(paragraph) <= self.character_limit:
            return paragraph
        
        paragraph_with_limit = paragraph[:self.character_limit]

        last_period = paragraph_with_limit.rfind('.')
        return paragraph_with_limit[: last_period + 1]
