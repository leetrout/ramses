from django.contrib import admin

from .models import *

class TeamAdmin(admin.ModelAdmin):
    """Adds slugify options to team admin form."""
    prepopulated_fields = {
        "slug": ("name",)
    }
    fields = ('name', 'slug', 'mascot')


class PlayerAdmin(admin.ModelAdmin):
    """Adds slugify options to player admin form."""
    prepopulated_fields = {
        "slug": ("last_name", "first_name",)
    }
    fields = ('team', 'first_name', 'last_name', 'slug')


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Sport)
