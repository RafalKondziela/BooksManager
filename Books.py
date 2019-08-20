class Book:

    def __init__(self, author, title, number_of_pages):
        self.author = str(author)
        self.title = str(title)
        self.number_of_pages = str(number_of_pages)

    def __str__(self):
        return "{} {} {}".format(self.author,self.title,self.number_of_pages)



    def show_Title(book):
        print(book.title)

    def addBook(library, length,book):
        library[int(length + 1)] = book

        
    
