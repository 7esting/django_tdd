from django.contrib import admin

# Register your models here.
from user_contacts.models import Person, Phone
from django.contrib import admin

admin.site.register(Person)
admin.site.register(Phone)