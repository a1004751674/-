from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from polls import models
from django.core import serializers
import json

# Create your views here.
def GetMedia(request):
    if request.method=="GET":
        data=models.Newsdata.objects.all()
    return JsonResponse(list(data.values()),safe=False)

def SearchMedia(request):
    request = request.GET.get('request')
    post_list = models.Newsdata.objects.filter(title__icontains=request).all()
    return JsonResponse(list(post_list.values()),safe=False)

def GetfrequencyTitle(request):
    if request.method=="GET":
        data=models.frequencytitle.objects.filter(frequency__gte=20).all()
    return JsonResponse(list(data.values()),safe=False)

def GetfrequencyContent(request):
    if request.method=="GET":
        data=models.frequencycontent.objects.filter(frequency__gte=20).all()
    return JsonResponse(list(data.values()),safe=False)