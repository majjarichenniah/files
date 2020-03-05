from django.db import models

# Create your models here.
class contactinfo(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    class Meta:
        abstract=True
class student(contactinfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()
class teacher(contactinfo):
    subject=models.CharField(max_length=100)
    salary=models.FloatField()

