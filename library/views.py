# library/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'biography']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'biography']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author_list')

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'published_date', 'isbn', 'summary']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date', 'isbn', 'summary']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
