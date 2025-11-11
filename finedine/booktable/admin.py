from django.contrib import admin
from booktable.models import booktable
# Register your models here.
class adminbooktable(admin.ModelAdmin):
    list_display=[
        'name',
        'email',
        'phone',
        'people',
        'date',
        'time',
        'message'
    ]
admin.site.register(booktable,adminbooktable)