# Command to retrieve the book instance and update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"  # Update the title attribute
book.save()  # Save the changes to the database

# Displaying the updated title to confirm the change
print(f"Updated Title: {book.title}")

# Expected Output:
# Updated Title: Nineteen Eighty-Four

