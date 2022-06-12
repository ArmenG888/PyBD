from django.shortcuts import render
from django.http import JsonResponse
from .models import Output

def home(request):
    return render(request, "backdoor/home.html")

def live_output_data(request):
    command_output = Output.objects.all().values()
    print(command_output)
    print(len(command_output))
    if len(command_output) != 0:
        return JsonResponse({"data":command_output})
    else:
        return JsonResponse({"data":0})