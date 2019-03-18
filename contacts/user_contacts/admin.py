from django.contrib import admin
from user_contacts.models import Person, Phone

# Register your models here.

# admin.site.register(Person)
# admin.site.register(Phone)

# Register models on /admin page.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'address', 'city', 'state', 'country']

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['person', 'number']
    