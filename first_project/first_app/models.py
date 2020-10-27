from django.db import models

# Create your models here.
class login(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 20)
    password = models.CharField(max_length = 15)

    def __str__(self):
        return self.name

class training(models.Model):
    domain = models.CharField(max_length = 20)

    def __str__(self):
        return self.domain

class candidate(models.Model):
    name = models.CharField(max_length = 30, unique=False)
    domain = models.ForeignKey('training', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Register(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.name