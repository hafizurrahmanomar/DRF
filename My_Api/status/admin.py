from django.contrib import admin
from .models import Status


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    #list_display as a builtin method
    list_display=['user','content','image']
    
    class Meta:
        Model=Status
        
admin.site.register(Status,StatusAdmin)
