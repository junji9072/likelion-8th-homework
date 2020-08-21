from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SCH(models.Model):
    image = models.ImageField(upload_to = 'images/',null=True)
    name = models.CharField(max_length = 20)
    major = models.CharField(max_length = 30)
    year = models.IntegerField()
    studentid= models.IntegerField()
    grade = models.IntegerField()
    GPA = models.FloatField()

    def __str__(self):
        return self.name