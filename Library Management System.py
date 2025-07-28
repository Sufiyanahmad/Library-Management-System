import json
import os

BOOKS_FILE = 'library_books.json'

# Load existing books from file or initialize empty list
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=4)

# Display all books
def display_books(books):
    if not books:
        print("\nNo books available.\n")
        return
    print("\nAvailable Books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. Title: {book['title']} | Author: {book['author']} | Status: {book['status']}")
    print()

# Add a new book
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    books.append({'title': title, 'author': author, 'status': 'Available'})
    save_books(books)
    print("✅ Book added successfully.\n")

# Borrow a book
def borrow_book(books):
    display_books(books)
    title = input("Enter the title of the book to borrow: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            if book['status'] == 'Available':
                book['status'] = 'Borrowed'
                save_books(books)
                print("✅ Book borrowed successfully.\n")
                return
            else:
                print("❌ Book is already borrowed.\n")
                return
    print("❌ Book not found.\n")

# Return a book
def return_book(books):
    title = input("Enter the title of the book to return: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            if book['status'] == 'Borrowed':
                book['status'] = 'Available'
                save_books(books)
                print("✅ Book returned successfully.\n")
                return
            else:
                print("❌ Book was not borrowed.\n")
                return
    print("❌ Book not found.\n")

# Delete a book
def delete_book(books):
    title = input("Enter the title of the book to delete: ").strip()
    for i, book in enumerate(books):
        if book['title'].lower() == title.lower():
            del books[i]
            save_books(books)
            print("✅ Book deleted successfully.\n")
            return
    print("❌ Book not found.\n")

# Menu-driven interface
def main():
    books = load_books()
    while True:
        print("=== Library Management System ===")
        print("1. Display All Books")
        print("2. Add New Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_books(books)
        elif choice == '2':
            add_book(books)
        elif choice == '3':
            borrow_book(books)
        elif choice == '4':
            return_book(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
