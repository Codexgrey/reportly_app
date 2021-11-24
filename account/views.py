from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Create your views here.
def password_isvalid(password):
    #password logic
    if (len(password) < 6) or (len(password) > 12):
        isValid = False
    elif not any(char.isdigit() for char in password): 
        isValid = False
    elif not any(char.islower() for char in password):
        isValid = False
    elif not any(char.isupper() for char in password):
        isValid = False
    else:
        isValid = True

    return isValid
    


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            # redirecting user to homepage, once verified
            return redirect('attendance:all_books')
        else:
            messages.warning(request, 'Please enter a valid username and password')

    return render(request, 'registration/login.html')


def signup_view(request):
    if request.method == "POST":
        data = {key:request.POST.get(key) for key in request.POST.keys()}

        if "csrfmiddlewaretoken" in data.keys():
            data.pop('csrfmiddlewaretoken')
        
        password = data.pop('password')
        re_password = data.pop('re_password')

        # confirming password
        if password == re_password:
            # check that password is valid and add to data if valid 
            if password_isvalid(password):
                data['password'] = make_password(password)
                # adding user to database via django User (model.Manager.create())
                try:
                    User.objects.create(**data, is_active=True)
                    messages.success(request, "Account created successfully!")
                except Exception:
                    messages.warning(request, "Username not available")
                    
            else:
                messages.warning(request, "Password length should be at least 6 and not more than 8 ")
                messages.warning(request, "Password should combine lowercase alphabet, uppercase alphabet and number")
        
        else:
            messages.warning(request, 'please enter matching passwords')

    return render(request, 'registration/signup.html')