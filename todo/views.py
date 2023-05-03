from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signupuser(request):
    form = UserCreationForm()
    return render(request, 'todo/signupuser.html', {'form': form})    