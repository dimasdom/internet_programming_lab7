from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'biography']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'summary']
