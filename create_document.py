import requests
from bs4 import BeautifulSoup
import wikipedia

class CreateDocument:
    wikipedia_url = 'https://en.wikipedia.org/wiki/Operating_system'
    document_save_path = ""
    character_limit = 1800 # the maximum length of a paragraph for a definition

    def __init__(self, document_save_path):
        self.document_save_path = document_save_path
        self.__create_document()

    def __create_document(self):
        unfiltered_html_content = self.__get_html_content(self.wikipedia_url)
        filtered_html_content = self.__get_filtered_html_content(unfiltered_html_content, 'contentSub', 'Notes')
        links = self.__get_links(filtered_html_content)
        for link in links:
            self.__write_first_paragraph_to_document(link, self.document_save_path)

    # returns a list of all the links from the html content provided
    def __get_links(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a') 
        links.pop(0) # first element is none
        links = [link for link in links if '/wiki/' in link.get('href') ] # remove non-wikipedia links
        return links

    # returns the html contents for the given url
    def __get_html_content(self, url):
        response = self.__get_http_request(url)
        html_content = response.content
        return html_content
    
    def __get_http_request(self, url):
        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.RequestException as e: 
            raise SystemExit(e)
        return response

    # returns a subsection of unfiltered_html_content containing information through start_id to (not including) end_id.
    # start_id and end_id are names of html ids within unfiltered_html_content.
    def __get_filtered_html_content(self, unfiltered_html_content, start_id, end_id):
        soup = BeautifulSoup(unfiltered_html_content, 'html.parser') # parse HTML content
        start = soup.find(id=start_id) 
        end = soup.find(id=end_id) 
        filtered_html_content = self.__remove_unnecessary_html(soup, start, end)
        return filtered_html_content

    # Removes unnecessary information such as citations, headers, etc...
    def __remove_unnecessary_html(self, soup, start, end):
        return str(start) + str(soup)[str(soup).index(str(start))+len(str(start)):str(soup).index(str(end))]

    # prints the first non-empty paragraph that appears in the html content provided
    def __write_first_paragraph_to_document(self, link, document_name):
        url_splits = link.get('href').split("/")
        wikipedia_page_name = url_splits[-1]

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
