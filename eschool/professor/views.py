from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def create_professor(request):
    return render(request, 'professor/new.html')