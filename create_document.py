import requests
from bs4 import BeautifulSoup
import wikipedia

class CreateDocument:
    wikipedia_url = 'https://en.wikipedia.org/wiki/Operating_system'
    document_save_path = ""

    def __init__(self, document_save_path):
        self.document_save_path = document_save_path
        self.__create_document()

    def __create_document(self):
        unfiltered_html_content = self.__get_html_content(self.wikipedia_url)
        filtered_html_content = self.__get_filtered_html_content(unfiltered_html_content, 'contentSub', 'Notes')
        links = self.__get_links(filtered_html_content)
        links = list(set(links)) # remove duplicate links
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
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e: 
            raise SystemExit(e)

        html_content = response.content
        return html_content

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
        wikipedia_page_name = url_splits[len(url_splits) - 1]
        try:
            wikipedia_page_summary = wikipedia.summary(wikipedia_page_name)
        except Exception:
            return
        first_paragraph = wikipedia_page_summary.split("\n")[0]
        document = open(document_name, 'a', encoding="utf-8")
        document.write(f"{wikipedia_page_name} : {first_paragraph} \n\n")
        document.close()
