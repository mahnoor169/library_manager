
# # Ye humari library hai, jismein books store karenge
# library = []




# # pheli book add krengy:
# book1 = {
#     "title" : "The Great Gatsby",
#     "author" : "F. Scott Fitzgerald",
#     "year" : 1925,
#     "genre" : "Fiction",
#     "read" : True                           # True ka matlab hai ki book padhi hui hai
# }




# #Dosri book add krengy:
# book2 = {
#     "title" : "1984",
#     "author" : "George Orwell",
#     "year" : 1949,
#     "genre" : "Dystopian",
#     "read" : False                  #False ka matlb h k book abhi nhi parhi
# }




# # Dono books ko library ma add krengy
# library.append(book1)
# library.append(book2)


# # library ko display krengy
# print("Your library:")
# for book in library:
#     print(book)



# # user se input lengy
# title = input("Enter the book title: ")
# author = input("Enter the author: ")
# year = int(input("Enter the publication year: "))
# genre = input("Enter the genre: ")
# read_status = input("Have you read this book? (Yes/no):").lower()== "yes"




# # nayi book dictionary bnaengy
# new_book = {
#     "title" : title,
#     "author" : author,
#     "year" : year,
#     "genre" : genre,
#     "read" : read_status
# }



# # Library ma add karengy
# library.append(new_book)
# print("Book added successfully!")



# # Updated library ko display karenge
# print("\nYour Library:")
# for book in library:
#     print(book)



# #  Menu System:-
# def main():
#     library = []           # Khali library banayi


#     while True:
#     # Menu display karenge
#     print("\nWelcome to My Personal Library Manager!")
#         print("1. Add a book")
#         print("2. Remove a book")
#         print("3. Search for a book")
#         print("4. Display all books")
#         print("5. Display statistics")
#         print("6. Exit")
#         choice = input("Enter your choice: ")


#         if choice == "1": add_book(library)
#         elif choice == "2": remove_book(library)
#         elif choice == "3": search_book(library)
#         elif choice == "4": display_books(library)
#         elif choice == "5": display_statistics(library)
#         elif choice == "6": print("Goodbye!")
#             break
#         else:
#             print("Invalid choice! Please try again.")



# # program start karengy
# if __name__ == "__main__":
#     main()




# # Ye humari library hai, jismein books store karenge
# library = []

# # Functions define karenge
# def add_book(library):
#     # User se input lenge
#     title = input("Enter the book title: ")
#     author = input("Enter the author: ")
#     year = int(input("Enter the publication year: "))
#     genre = input("Enter the genre: ")
#     read_status = input("Have you read this book? (Yes/no): ").lower() == "yes"

#     # Nayi book dictionary banayenge
#     new_book = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "genre": genre,
#         "read": read_status
#     }

#     # Library mein add karenge
#     library.append(new_book)
#     print("Book added successfully!")

# def remove_book(library):
#     title = input("Enter the title of the book to remove: ")
#     for book in library:
#         if book["title"].lower() == title.lower():
#             library.remove(book)
#             print(f"Book '{title}' removed successfully!")
#             return
#     print(f"Book '{title}' not found in the library.")

# def search_book(library):
#     title = input("Enter the title of the book to search: ")
#     for book in library:
#         if book["title"].lower() == title.lower():
#             print("Book found:")
#             print(book)
#             return
#     print(f"Book '{title}' not found in the library.")

# def display_books(library):
#     if not library:
#         print("Your library is empty!")
#     else:
#         print("\nYour Library:")
#         for book in library:
#             print(book)

# def display_statistics(library):
#     total_books = len(library)
#     read_books = sum(book["read"] for book in library)
#     unread_books = total_books - read_books

#     print("\nLibrary Statistics:")
#     print(f"Total books: {total_books}")
#     print(f"Books read: {read_books}")
#     print(f"Books unread: {unread_books}")

# # Menu System
# def main():
#     # Pehle se books add karenge
#     book1 = {
#         "title": "The Great Gatsby",
#         "author": "F. Scott Fitzgerald",
#         "year": 1925,
#         "genre": "Fiction",
#         "read": True
#     }
#     book2 = {
#         "title": "1984",
#         "author": "George Orwell",
#         "year": 1949,
#         "genre": "Dystopian",
#         "read": False
#     }
#     library = [book1, book2]  # Library initialize karenge

#     while True:
#         # Menu display karenge (sirf ek baar)
#         print("\nWelcome to My Personal Library Manager!")
#         print("1. Add a book")
#         print("2. Remove a book")
#         print("3. Search for a book")
#         print("4. Display all books")
#         print("5. Display statistics")
#         print("6. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_book(library)
#         elif choice == "2":
#             remove_book(library)
#         elif choice == "3":
#             search_book(library)
#         elif choice == "4":
#             display_books(library)
#         elif choice == "5":
#             display_statistics(library)
#         elif choice == "6":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice! Please try again.")

# # Program start karenge
# if __name__ == "__main__":
#     main()



# # Remove Book Feature
# def remove_book(library):
#     title = input("Enter the title of the book to remove: ")
#     for book in library:
#         if book["title"].lower() == title.lower():
#             library.remove(book)
#             print("Book removed successfully!")
#             return
#     print("Book not found!")



# # Search Book Feature
# def search_book(library):
#     print("Search by:")
#     print("1. Title")
#     print("2. Author")
#     search_choice = input("Enter your choice: ")

#     if search_choice == "1":
#         title = input("Enter the title: ")
#         for book in library:
#             if title.lower() in book["title"].lower():
#                 print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
#     elif search_choice == "2":
#         author = input("Enter the author: ")
#         for book in library:
#             if author.lower() in book["author"].lower():
#                 print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
#     else:
#         print("Invalid choice!")




# # Display Statistics Feature
# def display_statistics(library):
#     total_books = len(library)
#     if total_books == 0:
#         print("No books in the library!")
#         return
    
#     read_books = sum(book["read"] for book in library)
#     percentage_read = (read_books / total_books) * 100
    
#     print(f"Total books: {total_books}")
#     print(f"Percentage read: {percentage_read:.1f}%")





# # Library Manager Program

# # Library Manager Program

# def add_book(library):
#     title = input("Enter the book title: ")
#     author = input("Enter the author: ")
#     year = int(input("Enter the publication year: "))
#     genre = input("Enter the genre: ")
#     read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    
#     book = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "genre": genre,
#         "read": read_status
#     }
#     library.append(book)
#     print("Book added successfully!")

# def remove_book(library):
#     title = input("Enter the title of the book to remove: ")
#     for book in library:
#         if book["title"].lower() == title.lower():
#             library.remove(book)
#             print("Book removed successfully!")
#             return
#     print("Book not found!")

# def search_book(library):
#     print("Search by:")
#     print("1. Title")
#     print("2. Author")
#     search_choice = input("Enter your choice: ")
    
#     if search_choice == "1":
#         title = input("Enter the title: ")
#         for book in library:
#             if title.lower() in book["title"].lower():
#                 print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
#     elif search_choice == "2":
#         author = input("Enter the author: ")
#         for book in library:
#             if author.lower() in book["author"].lower():
#                 print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
#     else:
#         print("Invalid choice!")

# def display_books(library):
#     if not library:
#         print("Your library is empty!")
#     else:
#         print("Your Library:")
#         for i, book in enumerate(library, 1):
#             print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# def display_statistics(library):
#     total_books = len(library)
#     if total_books == 0:
#         print("No books in the library!")
#         return
    
#     read_books = sum(book["read"] for book in library)
#     percentage_read = (read_books / total_books) * 100
    
#     print(f"Total books: {total_books}")
#     print(f"Percentage read: {percentage_read:.1f}%")

# def save_library(library, filename="library.txt"):
#     try:
#         with open(filename, "w") as file:
#             for book in library:
#                 file.write(f"{book['title']},{book['author']},{book['year']},{book['genre']},{book['read']}\n")
#         print("Library saved to file. Goodbye!")
#     except Exception as e:
#         print(f"Error saving library: {e}")

# def main():
#     library = []  # Khali library banayi
    
#     while True:
#         # Menu display karenge
#         print("\nWelcome to your Personal Library Manager!")
#         print("1. Add a book")
#         print("2. Remove a book")
#         print("3. Search for a book")
#         print("4. Display all books")
#         print("5. Display statistics")
#         print("6. Exit")
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             add_book(library)
#         elif choice == "2":
#             remove_book(library)
#         elif choice == "3":
#             search_book(library)
#         elif choice == "4":
#             display_books(library)
#         elif choice == "5":
#             display_statistics(library)
#         elif choice == "6":
#             save_library(library)  # Exit se pehle library save karenge
#             break
#         else:
#             print("Invalid choice! Please try again.")

# # Program start karenge
# if __name__ == "__main__":
#     main()






# new code

import os  # File existence check ke liye

# File ka naam
FILENAME = "library.txt"

# Library ko file se load karne ka function
def load_library(filename=FILENAME):
    library = []
    if os.path.exists(filename):  # Check karna file exist karti hai ya nahi
        with open(filename, "r") as file:
            for line in file:
                title, author, year, genre, read = line.strip().split(",")
                library.append({
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "genre": genre,
                    "read": read.lower() == "true"
                })
    return library

# Library ko file me save karne ka function
def save_library(library, filename=FILENAME):
    with open(filename, "w") as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['genre']},{book['read']}\n")

# Book add karne ka function (File me bhi save karega)
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
    library.append(book)
    save_library(library)  # File update karna
    print("Book added successfully!")

# Book remove karne ka function (File me bhi update hoga)
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)  # File update karna
            print("Book removed successfully!")
            return
    print("Book not found!")

# Book search karne ka function
def search_book(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    search_choice = input("Enter your choice: ")
    
    if search_choice == "1":
        title = input("Enter the title: ")
        found_books = [book for book in library if title.lower() in book["title"].lower()]
    elif search_choice == "2":
        author = input("Enter the author: ")
        found_books = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("Invalid choice!")
        return

    if found_books:
        for book in found_books:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found!")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty!")
    else:
        print("Your Library:")
        for i, book in enumerate(library, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Display statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library!")
        return
    
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total_books) * 100
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Main function
def main():
    library = load_library()  # File se books load karna
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Program start karenge
if __name__ == "__main__":
    main()
