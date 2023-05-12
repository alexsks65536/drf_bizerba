"""
Класс содержит дополнительные переменные и таблицы БД,
которые подключаются к контексту в классах view
"""
from django.template import Template, Context
from .models import *


message = 'Нажмите на заголовок, чтобы отсортировать колонку!'


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        customer = Customer.objects.all()  # Контрагенты
        department = Department.objects.all() # Отдел
        installation = Installation.objects.all()  # установка ЗИП по заявке
        jobapplication = JobApplication.objects.filter(is_published=True)  # Заявка в работу
        logreceipt = LogReceipt.objects.filter(is_published=True)  # Журнал прихода ЗИП
        receiving = Receiving.objects.filter(is_published=True) # Приход ЗИП
        scalemodel = ScaleModel.objects.all()  # Модели весов
        serviceengineer = ServiceEngineer.objects.filter(is_published=True) # сервисный инженер
        sparepart = SparePart.objects.all()  # ЗИП

        context['customer'] = customer
        context['department'] = department
        context['installation'] = installation
        context['jobapplication'] = jobapplication
        context['logreceipt'] = logreceipt
        context['receiving'] = receiving
        context['scalemodel'] = scalemodel
        context['serviceengineer'] = serviceengineer
        context['sparepart'] = sparepart

        return context
