import os
from django.shortcuts import render
from django.views.generic import ListView

from .models import Scale
from .utils import DataMixin


class Index(ListView):
    template_name = 'mainapp/index.html'  # указываем путь к шаблону

    def get_queryset(self, *, object_list=None, **kwargs):
        return Scale.objects.all()


class Scales(ListView, DataMixin):
    # paginate_by = 10
    model = Scale
    template_name = 'mainapp/scales.html'  # указываем путь к шаблону
    context_object_name = 'scale'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # scale_all = Scale.objects.all()
        c_def = self.get_user_context(title=context['scale'])

        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def __mul__(self, other):
        return Index(self.value * other.value)

    def get_queryset(self, *, object_list=None, **kwargs):
        """
        Выбор отзывов, которые помечены для публикации
        """
        return Scale.objects.all()


class JobApplication(ListView, DataMixin):
    # paginate_by = 10
    model = Scale
    template_name = 'mainapp/jobapplication.html'  # указываем путь к шаблону
    context_object_name = 'scale'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['scale'])

        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def get_queryset(self, *, object_list=None, **kwargs):
        """
        Выбор отзывов, которые помечены для публикации
        """
        return Scale.objects.all()


class SparePart(ListView, DataMixin):
    # paginate_by = 10
    model = Scale
    template_name = 'mainapp/sparepart.html'  # указываем путь к шаблону
    context_object_name = 'scale'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['scale'])

        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def get_queryset(self, *, object_list=None, **kwargs):
        """
        Выбор отзывов, которые помечены для публикации
        """
        return Scale.objects.all()


class Receiving(ListView, DataMixin):
    # paginate_by = 10
    model = Scale
    template_name = 'mainapp/receiving.html'  # указываем путь к шаблону
    context_object_name = 'scale'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['scale'])

        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def get_queryset(self, *, object_list=None, **kwargs):
        """
        Выбор отзывов, которые помечены для публикации
        """
        return Scale.objects.all()


class Installation(ListView, DataMixin):
    # paginate_by = 10
    model = Scale
    template_name = 'mainapp/installation.html'  # указываем путь к шаблону
    context_object_name = 'scale'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['scale'])

        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def get_queryset(self, *, object_list=None, **kwargs):
        """
        Выбор отзывов, которые помечены для публикации
        """
        return Scale.objects.all()


