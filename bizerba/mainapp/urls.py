from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('scales/', Scales.as_view(), name='scales'),  # Весы
    path('jobs/', JobApplication.as_view(), name='jobs'),  # Заявки
    path('spare/', SparePart.as_view(), name='spare'),  # ЗИП
    path('receiving/', Receiving.as_view(), name='receiving'),  # Поступления ЗИП
    path('installation', Installation.as_view(), name='installation')  # Установки ЗИП
]
