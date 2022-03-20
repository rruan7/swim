from django.contrib import admin
from sets.models import Set

class SetAdmin(admin.ModelAdmin):
    list_display = ('category', 'distance', 'description')

# Register your models here.
admin.site.register(Set, SetAdmin)