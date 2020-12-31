from django.conf.urls import url, include
from mydb import views

app_name = 'mydb'

urlpatterns = [
    url(r'^$', views.front, name='front'),
    url('accounts', views.vault, name='vault'),
    url('formpage', views.form_name_view, name='form_name'),
    url('user', views.users_, name='index_urls'),
    url('signup', views.sign_up, name='signup'),
]
