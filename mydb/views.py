from django.shortcuts import render
from django.http.request import HttpRequest
from mydb.models import Account
from mydb.forms import UserProfileInfoForm, UserForm
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


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'mydb/signup.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})
