from django.shortcuts import render
from . models import (Employee,Value)
# Create your views here.
def index(request):
   value = Employee.objects.all()
   return render(request,'index.html',{'value':value})

from django.apps import apps
from django.contrib import admin


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)
