from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class WellnessScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    physical = models.IntegerField(default=0)
    intellectual = models.IntegerField(default=0)
    mental = models.IntegerField(default=0)
    social = models.IntegerField(default=0)
    spiritual = models.IntegerField(default=0)
    occupational = models.IntegerField(default=0)
    emotional = models.IntegerField(default=0)
    financial = models.IntegerField(default=0)
    environmental = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
