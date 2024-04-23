from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display=('id','name','created_date','isClosed')
    list_display_links=('id','name')
    list_filter=('id',)
    list_editable=('isClosed',)
    search_fields=('name','description')
    list_per_page=2

admin.site.register(Event,EventAdmin)
