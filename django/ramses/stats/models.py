from django.db import models

class Team(models.Model):
    """A basic model that represents a sports team."""
    name = models.CharField(max_length=100)
    mascot = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField()
    
    
class Player(models.Model):
    """A basic model that represents a player."""
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    team = models.ForeignKey("Team", related_name="players")
    slug = models.SlugField()


class Sport(models.Model):
    """A basic model that represents a sport."""
    name = models.CharField(max_length=100)
    slug = models.SlugField()
