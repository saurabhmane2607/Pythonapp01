from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=11)


class urls(models.Model):
    long_url = models.TextField()
    short_url = models.CharField(max_length=20)