from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Output, Computer

def home(request):
    context = {
        'computers': Computer.objects.all()
    }
    return render(request, "backdoor/home.html", context)

def computer_detail(request, pc_id):
    computer = Computer.objects.all().filter(id=pc_id)[0]
    return render(request, "backdoor/pc_detail.html", {'pc':computer})

def ajax(request, pk):
    data = ""
    computer = Computer.objects.all().filter(id=pk)[0]
    for output in Output.objects.all().filter(target=computer):
        data += output.target.pc_name + ":~$ " + output.output
    return JsonResponse({'data':data})