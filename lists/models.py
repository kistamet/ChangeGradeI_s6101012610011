from django.db import models
from django.db import models
class Userinfo(models.Model):
    #objects = None
    objects = None
    name = models.TextField(max_length=200, blank=True)
    #term1 = models.ManyToManyField('Term1')
   # term2 = models.ManyToManyField('Term2')
   # term3 = models.ManyToManyField('Term3')
   # term4 = models.ManyToManyField('Term4')
  #  term5 = models.ManyToManyField('Term5')
   # term6 = models.ManyToManyField('Term6')
    #term7 = models.ManyToManyField('Term7')
  #  term8 = models.ManyToManyField('Term8')
   # gpa = models.ManyToManyField('GPA')
    #password = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.name
class Term1(models.Model): #เก็บข้อมูลของ term1 โดยจะเก็บ subject unit Grade GPA
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)

class Term2(models.Model):#เก็บข้อมูลของ term2 โดยจะเก็บ subject unit Grade GPA
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term3(models.Model):#เก็บข้อมูลของ term3 โดยจะเก็บ subject unit Grade GPA
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term4(models.Model):#เก็บข้อมูลของ term4 โดยจะเก็บ subject unit Grade GPA
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term5(models.Model):#เก็บข้อมูลของ term5 โดยจะเก็บ subject unit Grade GPA
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)

class Term6(models.Model):#เก็บข้อมูลของ term6 โดยจะเก็บ subject unit Grade GPA
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term7(models.Model):#เก็บข้อมูลของ term7 โดยจะเก็บ subject unit Grade GPA
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class Term8(models.Model):#เก็บข้อมูลของ term8 โดยจะเก็บ subject unit Grade GPA
    subject = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
class GPA(models.Model):#เก็บข้อมูลของ term9 โดยจะเก็บ subject unit Grade GPA
    GPA_1 = models.CharField(max_length=255)
    GPA_2 = models.CharField(max_length=255)
    GPA_3 = models.CharField(max_length=255)
    GPA_4 = models.CharField(max_length=255)
    GPA_5 = models.CharField(max_length=255)
    GPA_6 = models.CharField(max_length=255)
    GPA_7 = models.CharField(max_length=255)
    GPA_8 = models.CharField(max_length=255)
