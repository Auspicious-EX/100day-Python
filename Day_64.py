# DAY 64 : Exercise 6 - Library Management System in Python 

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def display_books(self):
        if self.no_of_books == 0:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print("-", book)

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1
        print(f"Book '{book}' added successfully.")

    def get_no_of_books(self):
        return self.no_of_books


# Creating a library
library = Library()

# Displaying the initial state of the library
library.display_books()
print("Number of books initially:", library.get_no_of_books())

# Adding books to the library based on user input
while True:
    choice = input("Do you want to add a book? (yes/no): ").lower()
    if choice == "yes":
        book_name = input("Enter the name of the book: ")
        library.add_book(book_name)
    elif choice == "no":
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

# Displaying the final state of the library
library.display_books()
print("Number of books after adding:", library.get_no_of_books())
