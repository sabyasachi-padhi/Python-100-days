#in day 64 we are doing another excersize called library mangement system.......

#in day 67 we are going to slove excersize 6 ....
class library:
    def __init__(self):
        self.nobook=0
        self.book=[]

    def add_book(self , Book):
        self.book.append(Book)
        self.nobook=len(self.book)

    def show_info(self):
        print(f" The library has {self.nobook} books . the books are ")
        for book in self.book:
            print(book)


books = library()

books.add_book("python book for machine learning")
books.add_book("java book for App devlopment")
books.add_book("C++  book for DSA")

books.show_info()
        

    