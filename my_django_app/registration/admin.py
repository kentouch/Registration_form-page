from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'national_id', 'phone_number', 'organization', 'position')
    search_fields = ('firstname', 'lastname', 'email', 'national_id')
    list_filter = ('nationality', 'country_of_residence')