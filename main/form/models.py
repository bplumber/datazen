from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    github = models.TextField()
    first = models.CharField(max_length=15)
    second = models.CharField(max_length=15)
    third = models.CharField(max_length=15)

class Backend(models.Model):
    question = models.TextField()
    optiona = models.TextField()
    optionb = models.TextField()
    optionc = models.TextField()
    optiond = models.TextField()
    answer = models.TextField()

class Frontend(models.Model):
    question = models.TextField()
    optiona = models.TextField()
    optionb = models.TextField()
    optionc = models.TextField()
    optiond = models.TextField()
    answer = models.TextField()

class DataScience(models.Model):
    question = models.TextField()
    optiona = models.TextField()
    optionb = models.TextField()
    optionc = models.TextField()
    optiond = models.TextField()
    answer = models.TextField()

