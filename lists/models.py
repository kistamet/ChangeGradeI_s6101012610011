from django.contrib.auth.models import User
from django.db import models
class Datagrade(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    term = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    def __str__(self):
        return str(self.user)
class DataGPA(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    term_gpa = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
    def __str__(self):
        return str(self.user)