from django.shortcuts import render

from books.models import Book

# Create your views here.
def books(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        books = Book.objects.filter(title__icontains=searchTerm)
    else:
        books = Book.objects.all()
    return render(request, 'book.html', {'searchTerm': searchTerm,'books': books })
