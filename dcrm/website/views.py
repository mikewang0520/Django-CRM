from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout # http://localhost:8000/admin/
from django.contrib import messages

# Create your views here.
def home(request):

    return render(request, 'home.html', {})



def logout_user(request):
    pass
