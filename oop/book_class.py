class Book:
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year= year
        # destructor
    def __del__(self):
        print("Deleting (title of the book)")
    #string representation
    def __str__(self):
        return  "{title} by {author}, published in {year}"
    
    #official representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    