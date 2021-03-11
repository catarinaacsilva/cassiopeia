from django.db import models

class Create_User(models.Model):
    email = models.EmailField(unique = True)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    date = models.DateField()