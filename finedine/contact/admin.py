from django.contrib import admin
from contact.models import contactform
# Register your models here.
class admincontact(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message"]
admin.site.register(contactform, admincontact)