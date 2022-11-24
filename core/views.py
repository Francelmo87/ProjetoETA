from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


# @login_required
# def logout(request):
#     return redirect(request, 'registration/login.html')
