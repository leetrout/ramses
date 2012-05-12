from django.contrib import admin

from .models import *

class TeamAdmin(admin.ModelAdmin):
    """Adds slugify options to team admin form."""
    prepopulated_fields = {
        "slug": ("name",)
    }
    fields = ('entity', 'sport', 'name', 'slug', 'mascot')


class PlayerAdmin(admin.ModelAdmin):
    """Adds slugify options to player admin form."""
    prepopulated_fields = {
        "slug": ("first_name", "last_name")
    }
    fields = ('team', 'first_name', 'last_name', 'slug')


class SportAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Entity)
