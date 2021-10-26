from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    author = models.CharField(max_length=300)
    body = models.TextField()
    isbn = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=15)
    dob = models.CharField(max_length=24)
    age = models.IntegerField(default=18)
    track = models.CharField(max_length=50)
    mentor = models.CharField(max_length=50)
    goals = models.TextField()

    def __str__(self):
        return self.name
