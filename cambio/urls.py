from django.urls import path
from operaciones.views import dashboard, cotizar
urlpatterns=[path("",dashboard,name="dashboard"),path("cotizar/",cotizar,name="cotizar")]