from .views import *
from django.urls import path

urlpatterns = [
    path('list/',home, name='home'),
    path('', SenaCreate.as_view(), name='create'),
    path('<id>/',detail_view, name='detail'),

]