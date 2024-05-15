# library/urls.py
from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns
from .views import register
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import set_language
urlpatterns = [
    path('', views.AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/register/', register, name='register'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('users/<int:pk>/edit/', views.UserEditView.as_view(), name='user_edit'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('set-language/', set_language, name='set_language')
]
