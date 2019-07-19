from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=40,default="Anon")
    age=models.IntegerField(default=0)
    email=models.EmailField(default="anon@domain")
    password=models.CharField(max_length=50,null=True)
class Comments(models.Model):
    username=models.CharField(max_length=50,default="Anonymous")
    content=models.TextField()

def __str__(self):
    return self.username