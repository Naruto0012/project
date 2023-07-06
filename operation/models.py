from django.db import models

# Create your models here.

class StudentModel(models.Model):
    Name=models.CharField(max_length=100)
    Course=models.CharField(max_length=20)
    
    class Meta:
        db_table="student"
