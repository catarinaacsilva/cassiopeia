from django.db import models


class Create_User(models.Model):
    email = models.EmailField(unique = True, null=False, primary_key=True)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    datein = models.DateField()
    dateout = models.DateField()

class Create_Policy(models.Model):
    policyid = models.AutoField(primary_key=True)
    policy = models.CharField(max_length=1000, null = False)

class Consent_Reply(models.Model):
    consentid = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    consent = models.BooleanField()
    email = models.ForeignKey(Create_User, on_delete=models.CASCADE)
    policyid = models.ForeignKey(Create_Policy, on_delete=models.CASCADE)

class Device_Create(models.Model):
    deviceid = models.AutoField(primary_key=True)
    device = models.CharField(max_length=100)
    email = models.ForeignKey(Create_User, on_delete=models.CASCADE)
    policyid = models.ForeignKey(Create_Policy, on_delete=models.CASCADE)