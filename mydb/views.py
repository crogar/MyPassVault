from django.shortcuts import render
from django.http.request import HttpRequest
from mydb.models import Account
from mydb import forms


# Create your views here.


def front(request):
    return render(request, 'mydb/front.html', context=None)


def vault(request):
    accounts_list = Account.objects.order_by('url')
    passwords = {"accounts": accounts_list}
    return render(request, 'mydb/accounts.html', context=passwords)


def form_name_view(request):
    form = forms.FormName()
    return render(request, 'mydb/form.html', context={'form': form})

