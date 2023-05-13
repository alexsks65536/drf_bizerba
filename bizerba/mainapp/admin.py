from django.contrib import admin
from .models import *


# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address')
    list_display_links = ('title', 'address')
    search_fields = ('title', 'address')
    list_filter = ('title', 'address')
    # prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('title',)
    save_on_top = True


class ScaleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand')
    list_display_links = ('id', 'title', 'brand')
    search_fields = ('title', 'brand')
    list_filter = ('title', 'brand')
    save_on_top = True


class ScaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'scale_model', 'serial_number', 'scale_class', 'platform', 'ip_address')
    list_display_links = ('id', 'customer', 'scale_model', 'serial_number', )
    search_fields = ('id', 'customer', 'scale_model', 'serial_number', 'scale_class', 'platform',)
    list_filter = ('customer', 'scale_model', 'serial_number', 'scale_class', 'platform',)
    # prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class ServiceEngineerAdmin(admin.ModelAdmin):
    list_display = ('id', 'engineer')
    list_display_links = ('id', 'engineer')
    search_fields = ('id', 'engineer')
    list_filter = ('engineer',)
    # prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'time_create', 'customer', 'scale_model', 'serial_number')
    list_display_links = ('id', 'number', 'time_create', 'customer', 'scale_model', 'serial_number')
    search_fields = ('id', 'number', 'time_create', 'customer', 'scale_model', 'serial_number')
    list_filter = ('number', 'time_create', 'customer', 'scale_model', 'serial_number')
    # prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class SparePartAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor_code', 'title', 'scale_id', 'quantity')
    list_display_links = ('id', 'vendor_code', 'title', 'scale_id', 'quantity')
    search_fields = ('id', 'vendor_code', 'title', 'scale_id', 'quantity')
    list_filter = ('vendor_code', 'title', 'scale_id')
    # prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class ReceivingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'act_num', 'vendor_code', 'quantity', 'price', 'description')
    list_display_links = ('id', 'date', 'act_num', 'vendor_code', 'quantity', 'price', 'description')
    search_fields = ('id', 'date', 'act_num', 'vendor_code', 'quantity', 'price', 'description')
    list_filter = ('date', 'act_num', 'vendor_code', 'price', 'description')
    # prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class LogReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'date', 'customer')
    list_display_links = ('id', 'number', 'date', 'customer')
    search_fields = ('number', 'date', 'customer')
    list_filter = ('number', 'date', 'customer')
    # prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class InstallationAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_job', 'spare_part', 'quantity', 'time_create')
    list_display_links = ('id', 'number_job', 'spare_part', 'quantity', 'time_create')
    search_fields = ('id', 'number_job', 'spare_part', 'quantity', 'time_create')
    list_filter = ('number_job', 'spare_part', 'quantity', 'time_create')
    # prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


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
