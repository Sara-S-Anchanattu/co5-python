class publisher:
    def __init__(self,pubname):
        self.pubname=pubname

    def display(self):
        print("Publisher name is:", self.pubname)

class book(publisher):
    def  __init__(self,pubname, title,author):
        publisher.__init__(self,pubname)
        self.title=title
        self.author=author
    def display(self):
        print("Title", self.title)
        print("Author",self.author)
class python(book):
    def __init__(self,pubname,title,author,price,no_of_pages):
        book.__init__(self,pubname,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Publisher:",self.pubname)
        print("No.of pages:",self.no_of_pages)

b1= python("Alchemist","Paulo Choelo","DC","500","250")
b1.display()

