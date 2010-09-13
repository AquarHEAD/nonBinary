from nonBinary.lifestat.models import Stat
from django.contrib import admin

class StatAdmin(admin.ModelAdmin):
    list_display = ('content', 'stat_date')

admin.site.register(Stat, StatAdmin)