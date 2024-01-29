from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length = 100)
    nickname = models.CharField( max_length=100 default ='')
    image = models.ImageField(upload_to='student_images/')
    about = models.TextField(max_length = 10000)
    location = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 11)
    