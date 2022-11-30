from django.db import models

class student(models.Model):
    first_name= models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField()
    grade= models.IntegerField()

