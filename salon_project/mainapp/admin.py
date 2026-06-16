from django.contrib import admin
from mainapp.models import Services , Appointment

class ServicesAdmin(admin.ModelAdmin):
    list_display = ["services" , "duration" , "price"]
    
admin.site.register(Services , ServicesAdmin)
admin.site.register(Appointment)
