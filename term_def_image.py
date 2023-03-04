# A class that holds a term, its corresponding definition, and a link to an image of the term
class TermDefImage:
    term = ""
    definition = ""
    image_link = ""

    def __init__(self, term, definition, image_link):
        self.term = term
        self.definition = definition
        self.image_link = image_link