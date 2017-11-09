from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView
from django.db.models import Count
from .models import Book, Author
from .forms import ReviewForm
# Create your views here.


def review_books(request):
    """
    List all of the books that we want to review
    """
    books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books,
    }
    return render(request, "list-to-review.html", context)


def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)
    form = ReviewForm
    context = {
        'book': book,
        'form': form,
    }
    return render(request, "review-book.html", context)

def list_books(request):
    """
    List the books that have reviews
    :param request:
    :return:
    """
    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')
    context = {
        'books': books,
    }
    return render(request, "list.html", context)


class AuthorList(View):
    def get(self, request):
        authors = Author.objects.annotate(
            published_books=Count('books')
        ).filter(
            published_books__gt=0
        )
        context = {
            'authors': authors,
        }

        return render(request, "authors.html", context)


class BookDetail(DetailView):
    model = Book
    template_name = "book.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "author_detail.html"