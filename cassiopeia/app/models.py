from django.db import models

import uuid

class Create_User(models.Model):
    email = models.EmailField(unique = True, null=False, primary_key=True)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    datein = models.DateField()
    dateout = models.DateField()

class Create_Policy(models.Model):
    policyid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    policy = models.CharField(max_length=1000, null = False)

class Consent_Reply(models.Model):
    consentid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    status = models.CharField(max_length=10)
    email = models.ForeignKey(Create_User, on_delete=models.CASCADE)
    policyid = models.ForeignKey(Create_Policy, on_delete=models.CASCADE)