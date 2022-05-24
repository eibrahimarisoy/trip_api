from django.contrib import admin

from passengers.models import Passenger

# Register your models here.

class CustomPassengerAdmin(admin.ModelAdmin):
    search_fields = ('user__first_name', 'user__last_name', 'user__email')

admin.site.register(Passenger, CustomPassengerAdmin)