# Command to retrieve and display all attributes of the created book
book = Book.objects.get(title="1984")

# Displaying all attributes of the book instance
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

# Expected Output:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
