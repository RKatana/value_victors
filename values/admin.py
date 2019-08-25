from django.contrib import admin
from . models import (
   Value,
   Employee
)

class EmployeeAdmin(admin.ModelAdmin):
  
   pass
admin.site.register(Value)
admin.site.register(Employee, EmployeeAdmin)