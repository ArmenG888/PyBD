from django.shortcuts import render
from django.http import JsonResponse
from .models import Output

def home(request):
    return render(request, "backdoor/home.html")

