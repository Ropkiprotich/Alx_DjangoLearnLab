# Django Shell Commands for CRUD Operations on Book Model

# 1. Create a new book instance
book = Book(title="To Kill a Mockingbird", author="Harper Lee", publication_year=1960)
book.save()  # Save the new book to the database

# Expected Output:
# (no output for save, but the book instance is now stored in the database)


# 2. Retrieve the created book
retrieved_book = Book.objects.get(title="To Kill a Mockingbird")
print("Retrieved Book:", retrieved_book)

# Expected Output:
# Retrieved Book: <Book: To Kill a Mockingbird by Harper Lee, 1960>


# 3. Update the book's title
retrieved_book.title = "To Kill a Mockingbird (Updated Edition)"
retrieved_book.save()  # Save the updated title

# Confirm the update
updated_book = Book.objects.get(id=retrieved_book.id)
print("Updated Book Title:", updated_book.title)

# Expected Output:
# Updated Book Title: To Kill a Mockingbird (Updated Edition)


# 4. Delete the book instance
retrieved_book.delete()

# Confirm deletion by retrieving all books (expecting an empty result)
all_books = Book.objects.all()
print("All Books after Deletion:", list(all_books))

# Expected Output:
# All Books after Deletion: []
# (An empty list confirms that the book was successfully deleted)

