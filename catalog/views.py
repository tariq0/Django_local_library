from django.shortcuts import render
from django.shortcuts import reverse

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.views.generic import ListView
from django.views.generic import DetailView

from django.contrib.auth import logout
from.models import Book, Book_Instance, Author
from . import myforms

# Create your views here.


def index(request):
    """Home page"""

    books_count = Book.objects.all().count()
    authors_count = Author.objects.all().count()
    copies_count = Book_Instance.objects.all().count()

    visit_count = request.session.get('visit_count', 0)
    visit_count += 1
    request.session['visit_count'] = visit_count

    context = {
        'books_count':books_count,
        'authors_count':authors_count,
        'copies_count':copies_count,
        'visit_count':visit_count,
    }

    return render(request, 'catalog/index.html', context=context)


def log_out(request):
    """Log out view."""

    try:
        redirect_url = request.GET['next']
        logout(request)
        
        return HttpResponseRedirect(redirect_url)

    except KeyError:

        logout(request)
        return render(request, 'catalog/logged_out.html')



    
class BookListView(ListView):
    model = Book



class AuthorListView(ListView):
    model = Author



class BookDetailView(DetailView):
    model = Book



class AuthorDetailView(DetailView):
    model = Author



def borrowed_books(request):
    """Display borrowed books by users."""

    if request.user.is_authenticated:

        borrowed_books = request.user.book_instance_set.all()

        context = {
            'borrowed_books':borrowed_books,
        }
        return render(request, 'catalog/borrowed_books.html',context=context)

    else:
        redirect_url = reverse('login') + '?next=' + request.path 
        return HttpResponseRedirect(redirect_url)




def all_borrowed(request):
    """Shows all borrowed books for staff."""

    if request.user.is_staff:

        borrowed_books = Book_Instance.objects.filter(status__exact='o')
        context = {
            'borrowed_books':borrowed_books,
        }
        return render(request, 'catalog/all_borrowed.html', context=context)

    else:
        redirect_url = reverse('login') + '?next='+request.path
        return HttpResponseRedirect(redirect_url)




def due_back_renew(request, pk):
    """"To handle due back updation."""


    if request.method == 'GET':

        book = Book_Instance.objects.get(pk=pk)

        due_back = book.due_back

        form_data ={'due_back':due_back}

        form = myforms.RnewDueBack(form_data)

        context = {
            'form':form,
            'book':book,
        }

        return render(request, 'catalog/due_back_renew.html', context=context)

    else:
        
        form = myforms.RnewDueBack(request.POST)

        if form.is_valid():

            book = Book_Instance.objects.get(pk=pk)

            book.due_back = form.cleaned_data['due_back']

            book.save()

            return HttpResponseRedirect(reverse('catalog:all-borrowed'))

        else:

            book = Book_Instance.objects.get(pk=pk)

            context = {
            'form':form,
            'book':book,
            }

            return render(
                request, 
                'catalog/due_back_renew.html', 
                context=context
                )