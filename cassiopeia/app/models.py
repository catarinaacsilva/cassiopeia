from django.db import models
from jsonfield import JSONField

class User(models.Model):
    email = models.EmailField(unique = True, null=False, primary_key=True)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)

    def __str__(self):
      return self.email

class Stay(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    datein = models.DateField()
    dateout = models.DateField()
    
class Policy(models.Model):
    policyid = models.AutoField(primary_key=True)
    policy = models.CharField(max_length=1000, null = False)

    def __str__(self):
      return self.policy

class Device(models.Model):
    deviceid = models.AutoField(primary_key=True)
    device = models.CharField(max_length=100)
    policyid = models.ForeignKey(Policy, on_delete=models.CASCADE)


class Entity(models.Model):
    entityid = models.AutoField(primary_key=True)
    entity = models.CharField(max_length=100)
    policyid = models.ForeignKey(Policy, on_delete=models.CASCADE)


class Consent_Device(models.Model):
    consentid = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    consent = models.BooleanField()
    deviceid = models.ForeignKey(Device, on_delete=models.CASCADE)
    stayid = models.ForeignKey(Stay, on_delete=models.CASCADE)


class Consent_Entity(models.Model):
    consentid = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    consent = models.BooleanField()
    entityid = models.ForeignKey(Entity, on_delete=models.CASCADE)
    stayid = models.ForeignKey(Stay, on_delete=models.CASCADE)

class Receipt(models.Model):
    json_receipt = JSONField()
    timestamp_stored = models.DateTimeField(auto_now_add = True)
    timestamp_created = models.DateTimeField()
    stayid = models.ForeignKey(Stay, on_delete=models.CASCADE)

class Stay_Receipt(models.Model):
    stayid = models.ForeignKey(Stay, on_delete=models.CASCADE)
    receiptid = models.UUIDField()

    class Meta:
        unique_together = (('stayid', 'receiptid'),)