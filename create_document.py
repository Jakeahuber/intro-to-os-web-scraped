import os
import requests
from bs4 import BeautifulSoup
import wikipedia
from fpdf import FPDF

def main():
    url = 'https://en.wikipedia.org/wiki/Operating_system'
    document_name = 'intro_to_operating_systems.txt'
    unfiltered_html_content = get_html_content(url)
    filtered_html_content = get_filtered_html_content(unfiltered_html_content, 'contentSub', 'Notes')
    links = get_links(filtered_html_content)
    links = list(set(links)) # remove duplicate links
    for link in links:
        write_first_paragraph_to_document(link, document_name)

    create_pdf(document_name)
    os.remove(document_name) # remove txt file after pdf has been created

# returns a list of all the links from the html content provided
def get_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a') 
    links.pop(0) # first element is none
    links = [link for link in links if '/wiki/' in link.get('href') ] # remove non-wikipedia links
    return links

# returns the html contents for the given url
def get_html_content(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e: 
        raise SystemExit(e)

    html_content = response.content
    return html_content

# returns a subsection of unfiltered_html_content containing information through start_id to (not including) end_id.
# start_id and end_id are names of html ids within unfiltered_html_content.
def get_filtered_html_content(unfiltered_html_content, start_id, end_id):
    soup = BeautifulSoup(unfiltered_html_content, 'html.parser') # parse HTML content
    start = soup.find(id=start_id) 
    end = soup.find(id=end_id) 
    filtered_html_content = remove_unnecessary_html(soup, start, end)
    return filtered_html_content

# Removes unnecessary information such as citations, headers, etc...
def remove_unnecessary_html(soup, start, end):
    return str(start) + str(soup)[str(soup).index(str(start))+len(str(start)):str(soup).index(str(end))]

# prints the first non-empty paragraph that appears in the html content provided
def write_first_paragraph_to_document(link, document_name):
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

def create_pdf(document_name):
    pdf = FPDF()  
    pdf.add_page()

    # create title
    pdf.set_font('Arial', 'B', size = 15)
    pdf.cell(200, 10, txt="Intro to Operating Systems: Electric Boogaloo", ln = 1, align = 'C')

    # open the text file in read mode
    document = open(document_name, "r", encoding="utf-8")

    # insert the texts in pdf
    for paragraph in document:
        # need to change encoding so FPDF can read the contents
        paragraph = paragraph.encode('latin-1', 'replace').decode('latin-1')

        # don't include empty lines
        if (len(paragraph.split(":", 1)) == 1):
            continue

        term = paragraph.split(" : ", 1)[0].replace("_", " ")
        definition = paragraph.split(" : ", 1)[1] 

        pdf.set_font('Arial', 'B', size = 15)
        pdf.write(8, term)
        pdf.ln(10)

        pdf.set_font("Arial", size = 15)
        pdf.write(8, definition)
        pdf.ln(3)
    
    # save the pdf with name .pdf
    pdf.output("intro_to_operating_systems.pdf")  

if __name__ == "__main__":
    main()
