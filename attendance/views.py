from django.shortcuts import render, HttpResponse
from .models import Book


# Create your views here.
def test_view(request):
    myBooks = Book.objects.all()
    context = { 'books': myBooks }

    return render(request, 'test.html', context)

def home_page(request):
    return HttpResponse("I'm supposed to be the Home Page. 😒")