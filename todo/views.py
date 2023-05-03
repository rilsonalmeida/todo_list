from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'todo/home.html')


def signupuser(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'todo/signupuser.html', {
            'form': form,
            })    
    else:
        # Create a new user, if passwords match
        
        # We must check if a new user is not found in the database (to be implemented)
        input_username = request.POST['username']
        input_password1 = request.POST['password1']
        input_password2 = request.POST['password2']
        if input_password1 == input_password2:
            try:
                new_user = User.objects.create_user(input_username, password=input_password1)
                new_user.save()
                login(request, new_user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {
                            'form': UserCreationForm(),
                            'error': 'That username has already been taken. Please choose a new one.',
            })
        else:
            return render(request, 'todo/signupuser.html', {
            'form': UserCreationForm(),
            'error': 'Passwords did not match',
            })
        

def currenttodos(request):
    return render (request, 'todo/currenttodos.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:    
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/signupuser.html', {
                            'form': AuthenticationForm(),
                            'error': 'Invalid credentials',
            })
        else:
            login(request, user)
            return redirect('currenttodos')
