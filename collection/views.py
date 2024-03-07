

from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import generic
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from .models import *

def home_page(request):
    data = Person.objects.all()
    # select * from Person
    # return HttpResponse(data)
    return render(request, 'collection/home.html', {'data': data})

def find_person(request, id): 
    # SELECT * from Person where id = 1
    data = Person.objects.filter(id=id)
    return render(request, 'collection/home.html', {'data': data})

def api_person(request):
    data = Person.objects.all()
    dataset = {"results": list(data.values('first_name', 'last_name',
                                           'gender', 'dob', 'avatar',
                                           'contact', 'description'))}
    return JsonResponse(dataset)

