from django.contrib import admin
from .models import Stduent
# Register your models here.
@admin.register(Stduent)
class AdminStudent(admin.ModelAdmin):
    list_display=['id', 'name', 'age', 'email', 'phone_number']
