from django.contrib import admin

# Register your models here.
from .models import Team, Player


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','date_of_birth')
    fields = ['name', ('date_of_birth')]
#admin.site.register(Teacher)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player)