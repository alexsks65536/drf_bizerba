from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('scales/', Scales.as_view(), name='scales')
]