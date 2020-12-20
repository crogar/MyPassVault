from django.shortcuts import render
from django.http.request import HttpRequest


# Create your views here.

def front(request):
    return render(request, 'mydb/front.html', context=None)


