#DONE BY TUSIIME PRINCE B/23/U/D0621/PS, ARIGANYIRA CYRUS B/23/U/D0114/PS & ATUKWATSE MANZI ANTHLEM B/23/U/D0598/PS

# Program to greet the user and calculate their birth year
# This script asks for the user's name and age, then calculates their birth year

from datetime import datetime

# Get the user's name
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to our program.")

# Get the user's age with error handling for non-numeric input
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number for your age.")

# Calculate the birth year
current_year = 2024
birth_year = current_year - age
print(f"You were born in {birth_year}.")
# Extended program to check if the favorite number is even or odd

# Ask the user for their favorite number
while True:
    try:
        fav_number = int(input("Enter your favorite number: "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Check if the number is even or odd
if fav_number % 2 == 0:
    print(f"{fav_number} is an even number.")
else:
    print(f"{fav_number} is an odd number.")

# Chained and nested conditionals to compare the number with 10
if fav_number > 10:
    print("Your favorite number is greater than 10.")
elif fav_number < 10:
    print("Your favorite number is less than 10.")
else:
    print("Your favorite number is exactly 10.")

# Testing and Debugging (intentionally creating a variable name error)
try:
    print(fav_number)  # Intentional error: incorrect variable name
except NameError as e:
    print(f"Debugging error: {e}")
# Define a Book class with attributes and a method to describe the book

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        return f"{self.title} by {self.author}, published in {self.year}"

# Create two Book instances and display their descriptions
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("1984", "George Orwell", 1949)

print(book1.description())
print(book2.description())

# Function to sort books by publication year
def sort_books_by_year(book_list):
    if not book_list:
        print("The book list is empty.")
        return []
    return sorted(book_list, key=lambda x: x.year)

# Example book list and sorted display
book_list = [book1, book2]
sorted_books = sort_books_by_year(book_list)
for book in sorted_books:
    print(book.description())

# Advanced search functionality with iteration
while True:
    search_title = input("Enter a book title to search (or 'exit' to stop): ")
    if search_title.lower() == "exit":
        break
    found = False
    for book in book_list:
        if book.title.lower() == search_title.lower():
            print(f"Found: {book.description()}")
            found = True
            break
    if not found:
        print("Book not found.")
