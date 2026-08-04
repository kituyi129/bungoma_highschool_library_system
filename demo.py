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
        self.books=[] # isbn -> Book
              
    def add_book(self,book):  # add books to a dictionary stated above
        self.book=book
        self.books.append(book)  #intialize a key with ISBN in an empty list  
        print(f"Added a book:{book.title},{book.author},{book.isbn}, to a library")
 
    def checkout_book(self,isbn):
        self.isbn=isbn
        for book in self.books:
            if book.isbn==isbn and not book.is_checkout_book:
                book.is_checkout_book==True 
                print("you have borrowed",{book.title},{book.author},{book.isbn})
                return True
                print("book not available, or has been borrowed")
                    
        
    def return_book(self,isbn):
        self.isbn=isbn
        for book in self.books:
            if book.isbn==isbn:
                if book.checkout_book:
                    book.checkout_book=False
                    print("you have returned",{book.title})
                    return True
                    print("book not available, or has been borrowed")

    def list_books(self):
        if not self.books: ## checks if a list is empty
            print("No books in library")
            return
            
        for book in self.books:   ## loop for print list values
            print(book)
            
    #def find_by_author(self, author):
            
### create books from Book class       
book1=Book("software engineering","Charles megon","10000")
book2=Book("calculus","Grigorii jeff","10001")
book3=Book("E-commerce","Ken morris","10002")
book4=Book("Accounting","yunis musa","10003")

## creating objects from Library class
library=Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(Book("Java","ken","10005")) ## adding a book manually


## list library Books function
library.list_books()

library.checkout_book("10003")
library.checkout_book("10001")
library.checkout_book("10002")



#return books
return_book("10003") #changed return isdn
    
         
#def find_by_author(self, author):
# TODO
#    pass

#    def list_available_books(self):
list_books()# calling function to list all books in the library


