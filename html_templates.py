def get_start_html():
    return f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
</head>
    <body style="font-family:'Arial'">
        <h1 style="font-size: 45px; text-align: center; color: #000d33;"><b>Intro to OS: Web Scraped</b></h1>
        <h5 style="font-size: 25px; text-align: center; color: #000d33;">Author: Jake Huber (jah383@case.edu)</h5>
        <h3>Table Of Contents:</h3>
    """

    # removed div from bottom

def add_to_table_of_contents(term):
    return f"""
        <a href="#{term}" style="text-decoration: none;">{term}</a><br>
    """

def get_term_def_image_div(term, definition, image_link):
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

def get_end_html():
    return f"""
    </body>
</html>
"""

# removed div from top