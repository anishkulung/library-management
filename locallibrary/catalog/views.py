from django.shortcuts import render, get_object_or_404
from catalog.models import Author, Book, BookInstance, Genre
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

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

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing on loan to current user """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginated_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class AllBorrowedBooksListView(PermissionRequiredMixin, ListView):
    """Generic class-based view for books borrowed from library by all user """
    permission_required = ('catalog.can_mark_return')
    model = BookInstance
    template_name = 'catalog/all_borrowed_bookinstance_list.html'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

from catalog.forms import RenewBookForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_intance.save()
            return HttpResponseRedirect(reverse('all-borrowed'))

    else:
        proposed_renewal_date =  datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
    context = {
        'form': form,
        'book_instance': book_instance
    }
    return render(request, 'renew_book_librarian.html', context=context)