from django.urls import path
from .views import test_view, home_page


urlpatterns = [
    path("", home_page),
    path("about/", test_view)
]
