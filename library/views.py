# library/views.py
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .decorators import admin_required
from .models import CustomUser
from library.decorators import manager_required
from .models import Author, Book
from .forms import CustomUserChangeForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'

class AuthorCreateView(LoginRequiredMixin, CreateView):
    @method_decorator(manager_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorCreateView, self).dispatch(*args, **kwargs)
    model = Author
    fields = ['name', 'biography']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    @method_decorator(manager_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorUpdateView, self).dispatch(*args, **kwargs)
    model = Author
    fields = ['name', 'biography']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    @method_decorator(manager_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthorDeleteView, self).dispatch(*args, **kwargs)
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author_list')

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    @method_decorator(manager_required)
    def dispatch(self, *args, **kwargs):
        return super(BookCreateView, self).dispatch(*args, **kwargs)
    model = Book
    fields = ['title', 'author', 'published_date', 'isbn', 'summary']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(LoginRequiredMixin, UpdateView):
    @method_decorator(manager_required)
    def dispatch(self, *args, **kwargs):
        return super(BookUpdateView, self).dispatch(*args, **kwargs)
    model = Book
    fields = ['title', 'author', 'published_date', 'isbn', 'summary']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(LoginRequiredMixin,DeleteView):
    @method_decorator(manager_required)
    def dispatch(self, *args, **kwargs):
        return super(BookDeleteView, self).dispatch(*args, **kwargs)
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def monitor_session(request):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(monitor_session, self).dispatch(*args, **kwargs)
    entrance_time = request.session.get('entrance_time')
    if not entrance_time:
        request.session['entrance_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'monitor_session.html')



class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user_list.html'
    context_object_name = 'users'

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super(UserListView, self).dispatch(*args, **kwargs)

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books_url'] = reverse('book_list')
        context['authors_url'] = reverse('author_list')
        context['users_url'] = reverse('user_list')
        context['logout_url'] = reverse('logout')
        return context

class UserEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['username', 'role']
    template_name = 'user_edit.html'
    success_url = reverse_lazy('user_list')

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super(UserEditView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        obj = CustomUser.objects.filter(id=user_id).first()
        if not obj:
            raise Http404("No user found matching the query")
        return obj
    
    