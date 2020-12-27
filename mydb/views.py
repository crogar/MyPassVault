from django.shortcuts import render
from django.http.request import HttpRequest
from mydb.models import Account
from mydb.forms import NewUserForm
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

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # do something
            print("validation Success")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request, 'mydb/form.html', context={'form': form})


##########################################################################
# View that handles request to See signup.html                           #
##########################################################################


def users_(request):
    # passwords = {"accounts": accounts_list}
    return render(request, 'mydb/index.html')


def sign_up(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return users_(request)
        else:
            print("Something went wrong!")
    return render(request, 'mydb/signup.html', {'form': form})
