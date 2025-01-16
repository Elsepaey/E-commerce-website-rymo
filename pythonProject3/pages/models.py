from django.db import models
from datetime import datetime
# Create your models here.
class shoes (models.Model):
    name = models.CharField(max_length=20)
    describtion = models.TextField()
    publishdate = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to='photos')
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-publishdate']

class watches (models.Model):
    name = models.CharField(max_length=20)
    describtion = models.TextField()
    publishdate = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to='photos')
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-publishdate']

class dresses(models.Model):
    name = models.CharField(max_length=20)
    describtion = models.TextField()
    publishdate = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to='photos')
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-publishdate']

class bags (models.Model):
    name = models.CharField(max_length=20)
    describtion = models.TextField()
    publishdate = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to='photos')
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-publishdate']

class menshirts (models.Model):

    name = models.CharField(max_length=20)
    describtion = models.TextField()
    publishdate = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to='photos')
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-publishdate']