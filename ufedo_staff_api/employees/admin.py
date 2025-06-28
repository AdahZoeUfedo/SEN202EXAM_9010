from django.contrib import admin
from .models import StaffBase, Manager, Intern


admin.site.register(StaffBase)
admin.site.register(Manager)
admin.site.register(Intern)
