# Library Management System
import os
import time


# Book Class to define attributes of a book
class Book:
    def __init__(self, title, author, year, isbn, genre):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.genre = genre


# Library Class to manage books
class Library:
    def __init__(self):
        self.books = []

    # Function to add a new book to the library
    def add_book(self, title, author, year, isbn, genre):
        new_book = Book(title, author, year, isbn, genre)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added successfully!")

    # Function to delete a book from the library using its ISBN
    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN {isbn} deleted successfully!")
                return
        print(f"Book with ISBN {isbn} not found!")

    # Function to view all books in the library
    def view_books(self):
        if len(self.books) == 0:
            print("No books available in the library.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}, Genre: {book.genre}")

    # Function to search for books by title
    def search_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}, Genre: {book.genre}")
        else:
            print(f"No books found with title '{title}'.")

    # Function to search for books by author
    def search_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}, Genre: {book.genre}")
        else:
            print(f"No books found by author '{author}'.")

    # Function to search for books by genre
    def search_by_genre(self, genre):
        found_books = [book for book in self.books if genre.lower() in book.genre.lower()]
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}, Genre: {book.genre}")
        else:
            print(f"No books found in genre '{genre}'.")

    # Function to search for books by year
    def search_by_year(self, year):
        found_books = [book for book in self.books if book.year == year]
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}, Genre: {book.genre}")
        else:
            print(f"No books found from the year {year}.")

    # Function to search for books by ISBN
    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}, Genre: {book.genre}")
                return
        print(f"No book found with ISBN {isbn}.")
  

  

  

# Main Menu
def print_menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Delete a Book")
    print("3. View All Books")
    print("4. Search by Title")
    print("5. Search by Author")
    print("6. Search by Genre")
    print("7. Search by Year")
    print("8. Search by ISBN")
    print("9. Exit")


# User Input
def get_user_input():
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("Invalid choice, please select a number between 1 and 9.")
        except ValueError:
            print("Invalid input, please enter a valid number.")


# Main Application Loop
def main():
    library = Library()

    while True:
        print_menu()
        choice = get_user_input()

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter publication year: "))
            isbn = input("Enter ISBN number: ")
            genre = input("Enter book genre: ")
            library.add_book(title, author, year, isbn, genre)

        elif choice == 2:
            isbn = input("Enter ISBN of the book to delete: ")
            library.delete_book(isbn)

        elif choice == 3:
            library.view_books()

        elif choice == 4:
            title = input("Enter the title to search for: ")
            library.search_by_title(title)

        elif choice == 5:
            author = input("Enter the author to search for: ")
            library.search_by_author(author)

        elif choice == 6:
            genre = input("Enter the genre to search for: ")
            library.search_by_genre(genre)

        elif choice == 7:
            year = int(input("Enter the year to search for: "))
            library.search_by_year(year)

        elif choice == 8:
            isbn = input("Enter the ISBN to search for: ")
            library.search_by_isbn(isbn)

        elif choice == 9:
            print("Exiting the Library Management System. Goodbye!")
            break


# Run the program





if __name__ == "__main__":
    main()


explain rag_syn generate_answer