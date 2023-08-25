from django.db import models

class course(models.Model):
    id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=50)
    course_trainer=models.CharField(max_length=50)
    course_duration=models.CharField(max_length=10)
    course_fees=models.IntegerField()
    
    
class student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email_id=models.EmailField(max_length=50)
    Courses=models.ForeignKey(course, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.id} {self.name}'

# Create your models here.
