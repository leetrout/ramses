from django.db import models


class DatesBaseModel(models.Model):
    """Abstract base class to provide date fields."""
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class SlugBaseModel(models.Model):
    """Abstract base class for models with slugs"""
    slug = models.SlugField()
    
    class Meta:
        abstract = True


class Team(DatesBaseModel, SlugBaseModel):
    """A basic model that represents a sports team."""
    name = models.CharField(max_length=100)
    mascot = models.CharField(max_length=100, blank=True, null=True)
    sport = models.ForeignKey("Sport", related_name="teams")
    entity = models.ForeignKey("Entity", related_name="teams")
    
    def __unicode__(self):
        return self.name
    
    
class Player(DatesBaseModel):
    """A basic model that represents a player."""
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    team = models.ForeignKey("Team", related_name="players")
    slug = models.SlugField()
    
    def __unicode__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class Sport(DatesBaseModel):
    """A basic model that represents a sport."""
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name


class Entity(DatesBaseModel):
    """A basic model that represents a team owning entity."""
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name
   
