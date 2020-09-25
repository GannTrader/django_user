from django.contrib import admin
from django.contrib.auth.models import User
from .models import Employee
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class EmployeeAdmin(admin.StackedInline):
#     model = Employee
#     can_delete = True
#     verbose_name_plural = 'employee'
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (EmployeeAdmin,)
#
# admin.site.unregister(User)
admin.site.register(Employee)