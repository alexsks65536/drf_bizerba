from django.db import models


class Customer(models.Model):
    title = models.CharField(max_length=100, verbose_name='заказчик')
    address = models.CharField(max_length=255, blank=True, verbose_name='адрес заказчика')

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=128, verbose_name='отдел')

    def __str__(self):
        return self.title


class ScaleModel(models.Model):
    title = models.CharField(max_length=32, verbose_name='модель весов')
    brand = models.CharField(max_length=32, default='Bizerba')

    def __str__(self):
        return self.title


class Scale(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, null=True, verbose_name='заказчик')
    department = models.ForeignKey('Department', on_delete=models.PROTECT, null=True, verbose_name='отдел')
    scale_model = models.ForeignKey('ScaleModel', on_delete=models.PROTECT, null=True, verbose_name='модель весов')
    serial_number = models.CharField(max_length=16, null=True, verbose_name='серийный номер')
    comment = models.CharField(max_length=255, blank=True, verbose_name='описание')

    def __str__(self):
        return self.scaleModel


class JobApp(models.Model):
    number = models.IntegerField(verbose_name='заявка')
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, null=True, verbose_name='заказчик')
    scale_model = models.ForeignKey('ScaleModel', on_delete=models.PROTECT, null=True, verbose_name='модель весов')
    serial_number = models.CharField(max_length=16, null=True, verbose_name='серийный номер')
    defect = models.TextField(blank=True, verbose_name='неисправность')
    service_work = models.TextField(blank=True, verbose_name='выполненные работы')

    def __str__(self):
        return self.number


class ActArrival(models.Model):
    title = models.CharField(max_length='128', verbose_name='запчасть')
    vendor_code = models.CharField(max_length=16, verbose_name='артикул')
    quantity = models.IntegerField(default=0, verbose_name='остаток')
    description = models.CharField(max_length=255, blank=True, verbose_name='описание')
    scale_id = models.ForeignKey('ScaleModel', on_delete=models.PROTECT, null=True)


class SparePart(models.Model):
    title = models.CharField(max_length='128', verbose_name='запчасть')
    vendor_code = models.CharField(max_length=16, verbose_name='артикул')
    quantity = models.IntegerField(default=0, verbose_name='остаток')
    description = models.CharField(max_length=255, blank=True, verbose_name='описание')
    scale_id = models.ForeignKey('ScaleModel', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.vendor_code


class ActInstall(models.Model):
    number_job = models.ForeignKey('JobApp', verbose_name='заявка')
    spare_part = models.ForeignKey('SparePart')
    quantity = models.IntegerField(default=0, verbose_name='установлено')