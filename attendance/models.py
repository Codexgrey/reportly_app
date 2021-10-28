from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=15)
    dob = models.CharField(max_length=24)
    age = models.IntegerField(default=18)
    track = models.CharField(max_length=50)
    mentor = models.CharField(max_length=50)
    goals = models.TextField()
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    # student = models.OneToOneField(Student, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="books")
    author = models.CharField(max_length=300)
    body = models.TextField()
    isbn = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


