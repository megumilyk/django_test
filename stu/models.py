from django.db import models

# Create your models here.

class Stu(models.Model):
    fname = models.CharField(max_length=255,unique=1)
    fpwd = models.CharField(max_length=255)


    class Meta:
        db_table = 'stu'


class Studnet(models.Model):
    sno = models.AutoField(primary_key = True)
    sname = models.CharField(max_length=255)


    def __unicode__(self):
        return f'Student:{self.sname}'

    class Meta:
        db_table = 'student'

class Scard(models.Model):
    st = models.OneToOneField(Studnet,primary_key=True,on_delete=models.CASCADE)
    major = models.CharField(max_length=255)

    def __unicode__(self):
        return f'Scard:{self.major}'

    class Meta:
        db_table = 'scard'

