from django.conf.urls import url, include
from mydb import views

urlpatterns = [
    url(r'^$', views.front, name='front'),
    url('accounts', views.vault, name='vault'),
    url('formpage', views.form_name_view, name='form_name')
]
