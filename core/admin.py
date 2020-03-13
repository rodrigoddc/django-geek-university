from django.contrib import admin
from .models import Service, Role, Employee, Feature


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role', 'active', 'created', 'modified']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    fields = ['active', 'name', 'icon', 'description']
    list_display = ['name', 'icon', 'active', 'description', 'created', 'modified']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ['active', 'service', 'icon', 'description']
    list_display = ['service', 'icon', 'active', 'created', 'modified']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'active', 'created', 'modified']


