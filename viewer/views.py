from django.contrib.auth.decorators import login_required
from django.core.files import images
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from viewer.models import Category, Book


# Create your views here.

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        categories = Category.objects.filter(parent_category=None)

        context = {
            "images": images,
            "categories": categories,
        }
        return render(request, 'index.html', context)



class BookListView(View):
    template_name = "book_list.html"

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        books_in_category = category.book.all()
        context = {
            'category': category,
            'books': books_in_category,
        }
        return render(request, 'book_list.html', context)

class CategoryView(View):
    # template_name = "category.html"
    #
    # def get(self, request, pk):
    #     category = get_object_or_404(Category, id=pk)
    #
    #     books_in_category = Book.objects.filter(categories=category)
    #
    #     context = {
    #         "category": category,
    #
    #         "books_in_category": books_in_category,
    #     }
    #     return render(request, "category.html", context)
    template_name = "category.html"

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        books_in_category = category.books.all()
        print(books_in_category)
        context = {
            'category': category,
            'books': books_in_category,
        }
        return render(request, 'category.html', context)


class BookDetailView(View):
    template_name = "book_detail.html"

    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        context = {
            'book': book,
        }
        return render(request, 'book_detail.html', context)

def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.is_borrowed:
        # Kniha je už požičiavaná

        pass
    else:
        # Kniha nie je požičiavaná, označte ju ako požičiavanú
        book.is_borrowed = True
        book.owner = request.user
        book.save()

    return redirect('book_detail', pk=book_id)

@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.is_borrowed and book.owner == request.user:
        # Používateľ vrátil knihu
        book.is_borrowed = False
        book.owner = None
        book.save()

    return redirect('book_detail', pk=book_id)
