from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class member(models.Model):
    fname =models.CharField(max_length=50)
    lname =models.CharField(max_length=50)
    email =models.EmailField(max_length=100)
    passwd =models.CharField(max_length=10)
    age =models.PositiveIntegerField()

    def __str__(self) :
        return self.fname + ' ' + self.lname