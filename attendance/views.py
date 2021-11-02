from django.shortcuts import render, HttpResponse
from .models import Book


# Create your views here.
def test_view(request):
    all_books = Book.objects.all()
    context = { 'books': all_books }

    return render(request, 'test.html', context)

def home_page(request):
    return HttpResponse("I'm supposed to be the Home Page. 😒")