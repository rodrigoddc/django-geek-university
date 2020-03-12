from django.contrib import admin
from .models import Service, Role, Employee


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role', 'active', 'created', 'modified']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'icon', 'active', 'created', 'modified']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'active', 'created', 'modified']
