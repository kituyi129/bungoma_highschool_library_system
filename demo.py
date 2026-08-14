class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
            
    def __str__(self):
#  __ str__ is called double underscore. its user-friendly string representation of an object.
# TODO: return formatted string, e.g."'Dune' by Frank Herbert (Available)"
        return (f"library_book:{self.title},"
        f"Author:{self.author},"
        f"isbn:{self.isbn},"            
        f"checked_out:{'YES' if self.is_checked_out else 'NO'}") ##inline command  
        
class Library:
    def __init__(self):
        self.books={} # isbn -> Book
        
    def add_book(self,book):  # add books to a dictionary stated above
        self.book=book
        self.books[book.isbn]=book  #intialize a key with ISBN into a dcictionary  
        print(f"Added a book:{book.title},{book.author},{book.isbn}, to a library")

    
    def checkout_book(self,isbn):
        self.isbn=isbn
        if isbn in self.books:
            book = self.books[isbn]
            if not book.is_checked_out:
                book.is_checked_out=True 
                print(f"you have borrowed {book.title} by {book.author} ISBN: {book.isbn})")
                return True
            else:
                print("book not available, or has been borrowed")
                        
    def return_book(self,isbn):
        self.isbn=isbn
        for book in self.books:
            if book.isbn==isbn:
                if book.checkout_book:
                    book.checkout_book=False
                    
                    print("you have returned",{book.title})
                    return True
                else:
                    print("book not available, or has been borrowed")
                  
    
    def list_available_books(self):
        if not self.books: ## checks if a list is empty
            print("No books in library")
            return
        
        print("--------Available books in library:----------")
        for book in self.books.values():   ## loop for print list values
                print(book)
          
    def find_by_author(self, author):
            for book in self.books:
                if book.author==author:
                    print(book)
                    return True
                return False
            
### create books from Book class       
book1=Book("software engineering","Charles megon","100")
book2=Book("calculus","Grigorii jeff","101")
book3=Book("E-commerce","Ken morris","102")
book4=Book("Accounting","yunis musa","103")


## list library Books function
lib = Library()
lib.add_book(Book("Dune", "Frank Herbert", "111"))
lib.add_book(Book("Foundation", "Isaac Asimov", "222"))
lib.add_book(book1) #same as lib.add_book(Book("Dune", "Frank Herbert", "111"))
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)

print("-------------------added above books-----------------------------------------------")
print("-------------------added above books-----------------------------------------------")

lib.checkout_book("111")
lib.checkout_book("111") # should fail: already checked out
lib.checkout_book("999") # should fail: no such ISBN
print("--------------------borrowed above books-------------------------------------------")
print("--------------------borrowed above books-------------------------------------------")

lib.list_available_books() # should only show Foundation

print("--------------------available books above in library--------------------------------")
print("--------------------available books above in library--------------------------------")
lib.return_book("111")

print("-----------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------")
lib.list_available_books() # should show both again
