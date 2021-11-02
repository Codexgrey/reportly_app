from django.urls import path
from .views import test_view, home_page

app_name = 'attendance'
urlpatterns = [
    path("", home_page),
    path("books/", test_view, name='all_books')
]
