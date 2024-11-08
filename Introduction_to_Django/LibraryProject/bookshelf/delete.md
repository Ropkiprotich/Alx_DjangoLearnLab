# Command to retrieve the book instance and delete it
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()  # Delete the book from the database

# Confirming the deletion by retrieving all books
books = Book.objects.all()
print("All Books:", list(books))

# Expected Output:
# All Books: []
# (An empty list confirms that there are no books in the database)
