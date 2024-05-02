from django.contrib import admin
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author__name')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
