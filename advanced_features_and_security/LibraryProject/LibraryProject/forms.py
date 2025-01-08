from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search by title'})
    )
    author = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search by author'})
    )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'isbn']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'isbn': 'ISBN Number',
        }

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        if not isbn.isdigit() or len(isbn) != 13:
            raise forms.ValidationError("ISBN must be a 13-digit numeric value.")
        return isbn
