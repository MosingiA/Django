from django.contrib import admin
from .models import Club

# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'joined_date')
    search_fields = ('firstname', 'lastname', 'email')
admin.site.register(Club, ClubAdmin)
