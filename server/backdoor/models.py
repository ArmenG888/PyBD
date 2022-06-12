from django.db import models


class Computer(models.Model):
    ip_addr = models.CharField(default="192.168.1.1",max_length=12)
    pc_name = models.CharField(default="", max_length=100)


class Command(models.Model):
    command = models.CharField(default="", max_length=2000)
    target = models.ForeignKey(Computer, on_delete=models.CASCADE)

class Output(models.Model):
    command = models.CharField(default="", max_length=2000)
    output = models.TextField(default="", max_length=2000)
    target = models.ForeignKey(Computer, on_delete=models.CASCADE)
    time = models.DateTimeField()