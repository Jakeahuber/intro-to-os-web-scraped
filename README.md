## Intro to Operating Systems: Web Scraped 

This program builds a pdf document that contains the most important concepts/ideas of an introduction to OS course. 
It does this by web scraping the "Operating System" wikipedia page and pursues every linked term or phrase in a paragraph of text. It then takes the first paragraph of the linked page and appends that text to a pdf document. Inside the pdf, each term/phrase is accompanied by the first image that the Bing search engine finds for the term. 

## The Code

example.py contains an example of how the code is executed. It creates the files 'intro_to_os_web_scraped.txt' and 'intro_to_os_web_scraped.pdf', which are located within the repository. 

create_document.py contains the CreateDocument class that creates a text document of all the wikipedia terms and definitions to the document save path parameter.

create_pdf.py contains the CreatePdf class that generates a pdf file using the text document from CreateDocument. 

html_templates.py contains html text in the form of strings that we write to a temporary html file within CreatePdf. 

## Author

- [@Jake Huber](https://www.github.com/jakeahuber)