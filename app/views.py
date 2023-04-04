from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Programmer

# Create your views here.

def index(request):
    return render(request, "index.html")

def list_programmers(request):
    programers = list(Programmer.objects.values())
    data = {"programmers": programers}
    return JsonResponse(data)
