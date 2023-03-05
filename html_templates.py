class HtmlTemplate:
    start_html = f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
</head>
    <body style="font-family:'Arial';">
        <h1 style="font-size: 45px; text-align: center; color: #000d33;"><b>Intro to OS: Web Scraped</b></h1>
        <h5 style="font-size: 25px; text-align: center; color: #000d33;">Author: Jake Huber (jah383@case.edu)</h5>
        <img src="https://cdn.pixabay.com/photo/2013/07/13/11/43/tux-158547__340.png" alt="Tux Linux Logo" style="display: block; margin-top: 15%; margin-left: auto; margin-right: auto; width:80%;">     
    """

    start_page_div = f"""
        <div style="overflow:auto; page-break-before: always;">
     """
    
    table_of_contents_title = f"""
            <h2>Table Of Contents:</h2>    
    """

    start_column_div = f"""
            <div style="width: 50%;float: left;padding: 20px;">
    """

    def table_of_contents_link(term):
        return f"""
                <a href="#{term}" style="text-decoration: none;">{term}</a><br>
        """
    
    close_column_div = f"""
            </div>
    """

    close_page_div = f"""
        </div>
    """

    def term_def_image_div(term, definition, image_link):
        return f"""
        <div style="overflow:auto;">
            <div style="padding: 20px;">

                <div style="width: 50%;float: left;padding: 20px;">
                    <h1 style="color: #000d33;" id="{term}">{term}</h1>
                    <h5>{definition}</h5>
                </div>
                
                <div style="width: 50%;float: left;padding: 20px;">
                    <div>
                        <img src="{image_link}" alt="{definition}" style="width: 100%"/>
                    </div>
                </div>
            </div>
        </div>
        """

    end_html = f"""
    </body>
</html>
"""