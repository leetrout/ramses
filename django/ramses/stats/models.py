from django.db import models

class Team(models.Model):
    """A basic model that represents a sports team."""
    name = models.CharField(max_length=100)
    mascot = models.CharField(max_length=100, blank=True, null=True)
