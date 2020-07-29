from django.contrib import admin
from .models import Customer,Department,Logistics,Vehicle,Checklist


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','customer']

@admin.register(Logistics)
class LogisticsAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license']

@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ['logistics','department','delivery','receipt','items','number']
