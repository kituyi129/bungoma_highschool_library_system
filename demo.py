from unittest import case


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
    case "1":      
    def add_book(self,book):  # add books to a dictionary stated above
        self.book=book
        self.books[book.isbn]=book  #intialize a key with ISBN into a dcictionary  
        print(f"Added a book:{book.title},{book.author},{book.isbn}, to a library")

    case "2": 
    def checkout_book(self,isbn):
        self.isbn=isbn
        if isbn in self.books:
            book = self.books[isbn]
            if not book.is_checked_out:
                book.is_checked_out=True 
                print(f"you have borrowed {book.title} by {book.author} (ISBN: {book.isbn})")
                return True
            else:
                print("book not available, or has been borrowed")
                    
     case "3":     
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
    case "4":         
    def list_books(self):
        if not self.books: ## checks if a list is empty
            print("No books in library")
            return

            for book in self.books:   ## loop for print list values
                print(book)
    case "5":         
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

## creating objects from Library class
library=Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(Book("Java","ken","105")) ## adding a book manually


## list library Books function
library.list_books()

#check-out books from the library
library.checkout_book("103")
library.checkout_book("101")
library.checkout_book("102")
library.checkout_book("102")

#return books
library.return_book("103") 
 # calling function to list all books in the library         
library.list_books()

#additional menus function
    def menu(self):
        print("Welcome to Bungoma High School Library Management System")
        print("1. Add a book")
        print("2. Checkout a book")
        print("3. Return a book")
        print("4. List all books")
        print("5. Find books by author")
        print("6. Exit")

option=input("Enter your case choices  (1-5):")  
if case=="1":
    library.add_book()

elif case=="2":
    library.checkout_book()

elif case=="3":
    library.return_book()

elif case=="4":
    library.list_books()

elif case=="5":
    library.find_by_author()

else:
    print("Invalid option. Please try again.")






