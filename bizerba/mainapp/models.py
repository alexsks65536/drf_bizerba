from django.db import models


class Customer(models.Model):  # таблица контрагентов
    title = models.CharField(max_length=100, verbose_name='заказчик')
    address = models.CharField(max_length=255, blank=True, verbose_name='адрес заказчика')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        ordering = ['title']

    def __str__(self):
        return self.title


class Department(models.Model):  # таблица отделов
    title = models.CharField(max_length=128, verbose_name='отдел')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ['title']

    def __str__(self):
        return self.title


class ScaleModel(models.Model):  # таблица моделей весов
    title = models.CharField(max_length=32, verbose_name='модель весов')
    brand = models.CharField(max_length=32, default='Bizerba')

    class Meta:
        verbose_name = 'Модель весов'
        verbose_name_plural = 'Модели весов'
        ordering = ['title']

    def __str__(self):
        return self.title


class Scale(models.Model):  # таблица весов
    class ScaleClass(models.TextChoices):
        кг_3_6 = '3/6 кг'
        кг_6_15 = '6/15 кг'
        кг_15_30 = '15/30 кг'
        кг_30_60 = '30/60 кг'
        кг_60_150 = '60/150 кг'
        кг_600 = '600 кг'
        кг_1500 = '1500 кг'

    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, null=True, verbose_name='заказчик')
    department = models.ForeignKey('Department', on_delete=models.PROTECT, null=True, verbose_name='отдел')
    scale_model = models.ForeignKey('ScaleModel', on_delete=models.PROTECT, null=True, verbose_name='модель весов')
    serial_number = models.CharField(max_length=16, null=True, verbose_name='серийный номер')
    scale_class = models.CharField(max_length=32, null=True, choices=ScaleClass.choices, verbose_name='класс весов')
    ip_address = models.GenericIPAddressField(null=True, verbose_name='IP-адрес')
    comment = models.CharField(max_length=255, blank=True, verbose_name='примечание')

    class Meta:
        verbose_name = 'Весы'
        verbose_name_plural = 'Весы'
        ordering = ['customer', 'department', 'scale_model']

    def __str__(self):
        return self.scale_model


class ServiceEngineer(models.Model):  # таблица сервисных инженеров
    engineer = models.CharField(max_length=128, blank=True, verbose_name='сервисный инженер')
    time_create = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='изменен', auto_now=True)
    is_published = models.BooleanField(verbose_name='работает', default=True)
    to_remove = models.BooleanField(verbose_name='уволить', null=False, default=False)

    class Meta:
        verbose_name = 'Инженер'
        verbose_name_plural = 'Инженеры'
        ordering = ['engineer']

    def __str__(self):
        return self.engineer


class JobApplication(models.Model):  # таблица заявок в работу
    number = models.IntegerField(verbose_name='заявка')
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, null=True, verbose_name='заказчик')
    scale_model = models.ForeignKey('ScaleModel', on_delete=models.PROTECT, null=True, verbose_name='модель весов')
    serial_number = models.CharField(max_length=16, null=True, verbose_name='серийный номер')
    engineer = models.ForeignKey('ServiceEngineer', on_delete=models.PROTECT, null=True, verbose_name='сервисный инженер')
    defect = models.TextField(blank=True, verbose_name='неисправность')
    service_work = models.TextField(blank=True, verbose_name='выполненные работы')
    time_create = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='изменен', auto_now=True)
    is_published = models.BooleanField(verbose_name='опубликован', default=True)
    to_remove = models.BooleanField(verbose_name='удалить', null=False, default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['number', 'customer', 'time_create']

    def __str__(self):
        return self.number


class SparePart(models.Model):  # таблица перечень запчастей с артикулами
    title = models.CharField(max_length=128, verbose_name='запчасть')
    vendor_code = models.CharField(max_length=16, verbose_name='артикул')
    quantity = models.IntegerField(default=0, verbose_name='остаток')
    description = models.CharField(max_length=255, blank=True, verbose_name='описание')
    scale_id = models.ForeignKey('ScaleModel', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'ЗИП'
        verbose_name_plural = 'ЗИП'
        ordering = ['title', 'scale_id']

    def __str__(self):
        return self.vendor_code


class Receiving(models.Model):  # приход ЗИП
    act_num = models.ForeignKey('LogReceipt', on_delete=models.PROTECT)
    vendor_code = models.CharField(max_length=16, verbose_name='артикул')
    quantity = models.IntegerField(default=0, verbose_name='приход')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    scale_id = models.ForeignKey('ScaleModel', on_delete=models.PROTECT, null=True)
    description = models.CharField(max_length=255, blank=True, verbose_name='описание')
    time_create = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='изменен', auto_now=True)
    is_published = models.BooleanField(verbose_name='опубликован', default=True)
    to_remove = models.BooleanField(verbose_name='удалить', null=False, default=False)

    class Meta:
        verbose_name = 'Поступление ЗИП'
        verbose_name_plural = 'Поступление ЗИП'
        ordering = ['act_num', 'time_create']

    def __str__(self):
        return self.act_num


class LogReceipt(models.Model):  # журнал прихода ЗИП
    number = models.CharField(max_length=16, verbose_name='номер акта')
    date = models.DateField(verbose_name='дата акта')
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, null=True, default='Бицерба РУС')
    time_create = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='изменен', auto_now=True)
    is_published = models.BooleanField(verbose_name='опубликован', default=True)
    to_remove = models.BooleanField(verbose_name='удалить', null=False, default=False)

    class Meta:
        verbose_name = 'Реестр прихода ЗИП'
        verbose_name_plural = 'Реестр прихода ЗИП'
        ordering = ['number', 'date']

    def __str__(self):
        return self.number


class Installation(models.Model):  # реестр актов установки/расхода ЗИП по заявкам
    number_job = models.ForeignKey('JobApplication', on_delete=models.PROTECT, verbose_name='заявка')
    spare_part = models.ForeignKey('SparePart', on_delete=models.PROTECT, verbose_name='ЗИП')
    quantity = models.IntegerField(default=0, verbose_name='установлено')
    time_create = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='изменен', auto_now=True)
    is_published = models.BooleanField(verbose_name='опубликован', default=True)
    to_remove = models.BooleanField(verbose_name='удалить', null=False, default=False)

    class Meta:
        verbose_name = 'Установка ЗИП'
        verbose_name_plural = 'Установка ЗИП'
        ordering = ['number_job', 'time_create']

    def __str__(self):
        return self.number_job
