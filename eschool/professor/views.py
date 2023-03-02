from django.shortcuts import render
from django.http import HttpResponse
from professor.models import Proffesor
from pprint import pprint


# Create your views here.
def create_professor(request):
    profs = Proffesor.objects.all()
    return render(request, 'professor/new.html', {'professors' : profs})