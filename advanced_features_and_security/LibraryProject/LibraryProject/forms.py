from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter book title'})
    )
    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter author name'})
    )
    publication_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    isbn = forms.CharField(
        max_length=13,
        required=False,
        help_text="Optional. Enter a 13-digit ISBN."
    )
