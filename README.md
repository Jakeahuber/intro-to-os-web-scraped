# Intro to Operating Systems: Web Scraped 

This program builds a pdf document that contains the most important concepts/ideas of an introduction to OS course. 
It does this by web scraping the "Operating System" wikipedia page and pursues every linked term or phrase in a paragraph of text. It then takes the first paragraph of the linked page and appends that text to a pdf document. Inside the pdf, each term/phrase is accompanied by the first image that the Bing search engine finds for the term. 

## How To Use 

Refer to **example.py** 

## The Code

* **example.py** contains an example of how the code is executed. It creates the files 'intro_to_os_web_scraped.txt' and 'intro_to_os_web_scraped.pdf', which are located within the repository. 

* **create_document.py** contains the CreateDocument class that creates a text document with each linked term and corresponding definition from the "Operating System" wikipedia page. It saves the document to the "document_save_path" parameter. 

* **create_pdf.py** contains the CreatePdf class that creates a pdf file from an existing txt file made in create_document.py. The txt file is located at the "document_save_path" parameter. It saves the pdf file to the location of "pdf_save_path". It also takes in a parameter "path_to_wkhtmltopdf", which is the path to the user's wkhtmltopdf.exe file, which can be downloaded [here](https://wkhtmltopdf.org/). This file is necessary to convert the txt file into a pdf. 

* **html_templates.py** contains html text in the form of strings that we write to a temporary html file within CreatePdf. 

* **term_def_image.py** contains the TermDefImage class that holds a term, its corresponding definition, and a link to an image of the term. It is used within the CreatePdf class.

## Example Page

![example-page](https://user-images.githubusercontent.com/68114979/223008880-9f6cb8b8-a675-4e7a-bb50-1c5f3de1395f.png)

## Table of Contents 

![Screenshot 2023-03-06 171559](https://user-images.githubusercontent.com/68114979/223251997-2f4277d4-37a3-4d01-ad32-b83643bb1dc0.png)

## Front Page

![front-page](https://user-images.githubusercontent.com/68114979/222943840-c7dbf7b2-6523-47e9-9432-66cb532d110f.png)

## Author

- [@Jake Huber](https://www.github.com/jakeahuber)