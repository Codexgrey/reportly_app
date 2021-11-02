from django.contrib.auth import views
from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view , name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]