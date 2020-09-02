import requests
import xmltodict
import json
#import numpy as np
import urllib.request as ul
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
def index(request):
    url = 'http://openapi.seoul.go.kr:8088/47636346646e616b3132336c5066436f/xml/ListOnePMISBizInfo/1/5'
    request = ul.Request(url)
    response = ul.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        responseData = response.read()
        rD = xmltodict.parse(responseData)
        rDJ = json.dumps(rD)
        rDD = json.loads(rDJ)
        gs_data = rDD['ListOnePMISBizInfo']['row']
        pr
#    gs_data_dict = gs_data.flatten()
    #context = dict()
    #for i in gs_data:
    #    context['gs_data'] = gs_data
    #all_post = Post.objects.all()
    #context['all_post'] = all_post
    
    return render(request,'index.html', gs_data)
    
    
def detail(request):
#    context = dict()
 #   detail_post = Post.objects.get(id = post_id)
  #  context['detail_post'] = detail_post
    return render(request,'detail.html')
    
    