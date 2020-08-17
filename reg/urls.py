# Author:YK  gu
from django.urls import path

from . import views

urlpatterns=[
    path(r'',views.reg_view)

]