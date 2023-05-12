from django.contrib import admin
from .models import *


# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass


class ScaleModelAdmin(admin.ModelAdmin):
    pass


class ScaleAdmin(admin.ModelAdmin):
    pass


class ServiceEngineerAdmin(admin.ModelAdmin):
    pass


class JobApplicationAdmin(admin.ModelAdmin):
    pass


class SparePartAdmin(admin.ModelAdmin):
    pass


class ReceivingAdmin(admin.ModelAdmin):
    pass


class LogReceiptAdmin(admin.ModelAdmin):
    pass


class InstallationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(ScaleModel, ScaleModelAdmin)
admin.site.register(Scale, ScaleAdmin)
admin.site.register(ServiceEngineer, ServiceEngineerAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(SparePart, SparePartAdmin)
admin.site.register(Receiving, ReceivingAdmin)
admin.site.register(LogReceipt, LogReceiptAdmin)
admin.site.register(Installation, InstallationAdmin)
