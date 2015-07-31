#coding:utf-8
__author__ = 'wwl'
from django.shortcuts import render
from django.http import HttpResponse

def name(request):
    last_name=request.GET['last_name']
    first_name=request.GET['first_name']
    games=request.GET['games']
    foods=request.GET['foods']
    a1=int(request.GET['a1'])
    a2=int(request.GET['a2'])
    b1=int(request.GET['b1'])
    b2=int(request.GET['b2'])
    name='你的姓名是：'+last_name+first_name+'<br>'
    favorite='你的爱好：'+games+'<br>你喜欢的食物：'+foods+'<br>'
    people='能投入战斗的共有'+str(a1*a2+b1*b2)+'人。'
    return HttpResponse(name+favorite+people)
