from django.db import models
from django import forms

# Create your models here.


# This file contains a class that inherits ModelForm and mention the model name for which HTML form is created.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    # This under calss need for create Model forms!!!
    class Meta:
        db_table = 'student'


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    econtact = models.CharField(max_length=5000)
    class Meta:
        db_table = 'employee'

# Next two Classes are for Foreign key test.
class Auther(models.Model):  
    eid = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    email = models.EmailField()  

    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)  
  
class Post(models.Model):  
    title = models.CharField(max_length=100)  
    # Here we define the on_delete as CASCADE  
    author = models.ForeignKey(Auther, on_delete=models.CASCADE)  
  
    def __str__(self):  
        return self.title  
