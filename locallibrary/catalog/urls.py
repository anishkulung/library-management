from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.AllBorrowedBooksListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create',views.AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>',views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/delete/<int:pk>',views.AuthorDeleteView.as_view(), name='author_delete'),
    path('book/create',views.BookCreateView.as_view(), name='book_create'),
    path('book/update/<int:pk>',views.BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>',views.BookDeleteView.as_view(), name='book_delete'),
]
