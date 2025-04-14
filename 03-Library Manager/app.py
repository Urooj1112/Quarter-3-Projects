import streamlit as st
import json

# Define the file where the book library will be stored
library_file = "library.txt"

def load_library(fileName):
    """Load the library from a file. If the file doesn't exist or is empty, return an empty list."""
    try:
        with open(fileName, "r") as file:
            return json.load(file)  # Load book data from the file
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []  # Return an empty list if the file is missing or has invalid content

def save_books(fileName, books):
    """Save the current book list to the file."""
    with open(fileName, "w") as file:
        json.dump(books, file, indent=4)  # Save data in a readable JSON format

def display_menu():
    """Show the main menu with available options."""
    st.markdown("###  Welcome LibroNest!  A cozy home for all your books. ")
    st.write("Choose an option below:")
    
    menu_options = [
        "Add a Book",
        "Remove a Book",
        "Search for a Book",
        "Display All Books",
        "Display Statistics"
    ]
    choice = st.radio("Options", menu_options)
    return choice

def add_book(all_books: list):
    """Allow the user to add a new book to the library."""
    st.subheader("Add a New Book ")
    title = st.text_input("Enter Title: ")
    author = st.text_input("Enter Author: ")

    year = st.number_input("Enter Publication Year:", min_value=1000, max_value=9999)
    genre = st.text_input("Enter Genre: ")
    read_status = st.radio("Have you read this book?", ("Yes", "No"))
    read_status = True if read_status == "Yes" else False

    if st.button("Add Book"):
        if title and author and year and genre:
            new_book = {
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "read": read_status
            }
            all_books.append(new_book)
            save_books(library_file, all_books)
            st.success(f" '{title}' by {author} added to your library!")
        else:
            st.error(" Please fill in all fields to add a book.")

def remove_book(all_books: list):
    """Remove a book from the library by title."""
    st.subheader("Remove a Book ")
    book_to_remove = st.text_input("Enter the title of the book to remove:")

    if st.button("Remove Book"):
        for book in all_books:
            if book["title"].lower() == book_to_remove.strip().lower():
                all_books.remove(book)
                save_books(library_file, all_books)
                st.success(f"✅ '{book_to_remove}' has been removed from your library!")
                break
        else:
            st.error(" Book not found in the library.")

def search_book(all_books):
    """Search for a book by title or author."""
    st.subheader("Search for a Book 🔍")
    search_type = st.radio("Search by:", ("Title", "Author"))
    
    search_query = st.text_input(f"Enter the {search_type}:")
    if st.button("Search"):
        if search_query:
            results = []
            if search_type == "Title":
                results = [book for book in all_books if book["title"].lower() == search_query.strip().lower()]
            elif search_type == "Author":
                results = [book for book in all_books if book["author"].lower() == search_query.strip().lower()]
            
            if results:
                st.write(f"**Found {len(results)} matching book(s):**")
                for book in results:
                    read_status = "Read" if book["read"] else "Unread"
                    st.write(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Status: {read_status}")
            else:
                st.error(" No books found matching your search.")
        else:
            st.error(" Please enter a valid search term.")

def display_books(all_books):
    """Display all books in the library."""
    st.subheader("Your Library 📚")
    if all_books:
        for book in all_books:
            read_status = "Read" if book["read"] else "Unread"
            st.write(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Status: {read_status}")
    else:
        st.write("❌ Your library is empty.")

def display_statistics(all_books):
    """Show statistics about the user's library."""
    st.subheader("Library Statistics 📊")
    total_books = len(all_books)
    read_books = sum(1 for book in all_books if book["read"])

    if total_books == 0:
        st.write(" Your library is empty.")
    else:
        read_percentage = (read_books / total_books) * 100
        st.write(f"Total books: {total_books}")
        st.write(f"Books read: {read_books} ({read_percentage:.2f}%)")
        st.write(f"Books unread: {total_books - read_books} ({100 - read_percentage:.2f}%)")

def main():
    """Main function to run the library manager."""
    all_books: list = load_library(library_file)  # Load books from the file
    
    choice = display_menu()
    
    if choice == "Add a Book":
        add_book(all_books)
    elif choice == "Remove a Book":
        remove_book(all_books)
    elif choice == "Search for a Book":
        search_book(all_books)
    elif choice == "Display All Books":
        display_books(all_books)
    elif choice == "Display Statistics":
        display_statistics(all_books)

if __name__ == "__main__":
    main()

# --- Footer ---
st.markdown("""
    <br><hr>
    <div style="text-align: center; font-size: 14px; color: gray;">
         Built with love by <b>Urooj Saeed</b> | Library Manager
    </div>
""", unsafe_allow_html=True)
