from django.conf.urls import url, include
from mydb import views

urlpatterns = [
    url(r'^$', views.front, name='front'),
    url('accounts', views.vault, name='vault')
]
