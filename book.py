class publisher:
    def __init__(self,pubname):
        self.pubname=pubname

    def display(self):
        print("publi name : ",self,pubname)

class book(publisher):
    def __init__(self,pubname,title,author):
        publisher.__init__(self,pubname)
        self.author=author
        self.title=title

    def display(self):
        print("title",self.title)
        print("author",self.author)

class python(book):
    def __init__(self,pubname,title,author,price,pages):
        book.__init__(self,pubname,title,author)
        self.price=price
        self.pages=pages

    def display(self):
        print("title",self.title)
        print("author",self.author)
        print("publisher name",self.pubname)
        print("pricr",self.price)
        print("no.of pages",self.pages)
b1=python("alchemist","paulo coehlo","dc","500","250")
b2=book("dc","harrypotter","jk rowling")
b2.display()
b1.display()
