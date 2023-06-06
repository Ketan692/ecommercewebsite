from django.contrib import admin
from accounts.models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "address", "state", "city", "mobile")

admin.site.register(Address, AddressAdmin)

# Register your models here.
