from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"hey so im coming from first_app\index.html file so ya lesgooo"}
    return render(request, 'first_app\index.html', context=my_dict)
