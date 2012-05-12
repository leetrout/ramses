from django.contrib import admin

from .models import *

class TeamAdmin(admin.ModelAdmin):
    """Adds slugify options to team admin form."""
    prepopulated_fields = {
        "slug": ("name",)
    }
    fields = ('name', 'slug', 'mascot')


admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
admin.site.register(Sport)
