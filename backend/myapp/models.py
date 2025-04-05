from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Trainers(models.Model):
    trainer_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='trainers')
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.trainer_name

class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.course_name


class ClassStatus(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class ClassName(models.Model):
    class_name = models.CharField(max_length=255)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True)
    trainer = models.ForeignKey(Trainers, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    class_status = models.ForeignKey(ClassStatus, on_delete=models.CASCADE, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.class_name
    
class StudentsEnroll(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    enroll_date = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.usr.username