class Book:
    print("-------------Nairobi School Library system-------------")
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
        """Add a book to the library."""
        self.book=book
        self.books[book.isbn]=book  #intialize a key with ISBN into a dcictionary  
        print(f"Added a book:{book.title},{book.author},{book.isbn}, to a library")

    
    def checkout_book(self,isbn):
        print("----------------- Library checkout Catalog---------------------")
        self.isbn=isbn
        if isbn in self.books:
            book = self.books[isbn]
            if not book.is_checked_out:
                book.is_checked_out=True 
                print(f"you have borrowed {book.title} by {book.author} (ISBN: {book.isbn})")
                return True
            
            else:
                print("book not available, or has been borrowed")

            if isbn not in self.books:
                print("isbn not found in library")
                return      
        
    def return_book(self,isbn):
        self.isbn=isbn
        for book in self.books:
            if book.isbn==isbn:
                if book.checkout_book:
                    book.checkout_book=False
                    print("you have returned",{book.title})
                    return True
                    print("book not available, or has been borrowed")

               
    def find_by_author(self, author):
        for book in self.books:
            if book.author==author:
                print(book)
                return
                
    def list_available_books(self):
        if not self.books: ## checks if a list is empty
            print("No books in library")
            return
        print("----------------- Library books Catalog---------------------")
   
        for book in self.books.values():   ## loop for print list values
            print(book)
           
### create books from Book class       
book1=Book("software engineering","Charles megon","100")
book2=Book("calculus","Grigorii jeff","101")
book3=Book("E-commerce","Ken morris","102")
book4=Book("Accounting","yunis musa","103")

## creating objects from Library class
library=Library()
library.add_book(book1)
library.add_book(book2)

## adding a book manually to a library list
library.add_book(Book("Java","ken","10005")) 
library.add_book(Book("Dune", "Frank Herbert", "111"))
library.add_book(Book("Foundation", "Isaac Asimov", "222"))

# checking out/ borrowing books from Library
library.checkout_book("111")
library.checkout_book("111") # should fail: already checked out
library.checkout_book("999") # should fail: no such ISBN

library.list_available_books() # should only show Foundation

library.return_book("111")

library.list_available_books() # should show both again
library.find_by_author(101)

