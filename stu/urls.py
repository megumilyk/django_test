# Author:YK  gu
from django.urls import path

from . import views


urlpatterns = [
    path('',views.index_view),
    path(r'login/',views.login_view),
    path(r'register/',views.register_view),
    path(r'show/',views.show_view),
]