from django.shortcuts import render, get_object_or_404
from catalog.models import Author, Book, BookInstance, Genre
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
	''' view function for home page of site'''
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()
	num_visits = request.session.get('num_visits',0)
	request.session['num_visits'] = num_visits + 1
	context = {
		'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
	}
	return render(request, 'index.html', context=context)

class BookListView(ListView):
	model = Book
	context_object_name = 'book_list'
	queryset = Book.objects.filter()[:]
	template_name = 'catalog/books_list.html'

class BookDetailView(DetailView):
	model = Book

class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'catalog/authors_list.html'

class AuthorDetailView(DetailView):
    model = Author