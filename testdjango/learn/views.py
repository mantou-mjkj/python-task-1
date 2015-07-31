# coding:utf-8
from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse

def home(request):
    string='i am a test string'
    list=['于','洁','third']
    list1=('list1','list2')
    return render(request,'home.html',{
        'list':json.dumps(list),
        'list1':json.dumps(list1)
    })