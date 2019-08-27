"""Catalog App url config"""

from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path(
        'author/<int:pk>/', 
        views.AuthorDetailView.as_view(), 
        name='author-detail'
        ),
    path('borrowed-books/', views.borrowed_books, name='borrowed-books'),
    path('log-out/', views.log_out, name='log-out'),
    path('all-borrowed/', views.all_borrowed, name='all-borrowed'),
    path('due-back-renew/<uuid:pk>', views.due_back_renew, name='due-back-renew'),
]