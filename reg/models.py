from django.db import models


# Create your models here.


class Classmate(models.Model):
    cno = models.AutoField(primary_key=True)
    clsname = models.CharField(max_length=255)

    def __str__(self):
        return f'Classmate:{self.clsname}'


class Course(models.Model):
    curno = models.AutoField(primary_key=True)
    curname = models.CharField(max_length=255)

    def __str__(self):
        return f'student:{self.curname}'


class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=255)
    cn = models.ForeignKey(Classmate,on_delete=models.CASCADE)
    cour = models.ManyToManyField(Course)

    def __str__(self):
        return f'student:{self.sname}'
