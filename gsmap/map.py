import requests
import pandas as pd
from bs4 import BeautifulSoup
#import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from django.shortcuts import render,redirect
import requests
import xmltodict
import json
#import numpy as np
import urllib.request as ul
from django.contrib.auth import get_user_model
from django.db.models import Q


#def make_map(request, sigun, bjdong, bun, ji):

#startnumber = 1
#endnumber = 1000
#GsData = {}

open_api_key = unquote('LRz1LCEBA4jbTvkY9e9aOlDhER1Px4NShhPOt69D975W82kzo6kt5MIaI7AeqPICS%2BYjfpc3xXo8yPEP2dsLHQ%3D%3D') #decode
url = 'http://apis.data.go.kr/1611000/BldRgstService/getBrRecapTitleInfo'
queryParams = '?' + urlencode(
    {
        quote_plus('ServiceKey') : open_api_key,
        quote_plus('sigunguCd') : '11680',
        quote_plus('bjdongCd') : '10600',
        quote_plus('platGbCd') : '0',
        quote_plus('bun') : '',
        quote_plus('ji') : '',
        quote_plus('startDate') : '',
        quote_plus('endDate') : '',
        quote_plus('numOfRows') : '10000',
        quote_plus('pageNo') : '1' 
        
    }
    )
requests = ul.Request(url + queryParams)
response = ul.urlopen(requests)
rescode = response.getcode()
context = {}

if(rescode==200):
    responseData = response.read()
    rD = xmltodict.parse(responseData)
    rDJ = json.dumps(rD)
    rDD = json.loads(rDJ)
    gs_data = rDD['response']['body']['items']['item']
    gs_dict = gs_data
    context["gs_context"] = gs_dict
    context["gs_center"] = gs_dict[0]
    print(gs_dict)
    print(gs_dict[0])
    print(context["gs_context"])

#open_api_key = unquote('LRz1LCEBA4jbTvkY9e9aOlDhER1Px4NShhPOt69D975W82kzo6kt5MIaI7AeqPICS%2BYjfpc3xXo8yPEP2dsLHQ%3D%3D') #decode
#url = 'http://apis.data.go.kr/1611000/BldRgstService/getBrRecapTitleInfo'
#queryParams = '?' + urlencode(
#    {
#        quote_plus('ServiceKey') : open_api_key,
#        quote_plus('sigunguCd') : '11680',
#        quote_plus('bjdongCd') : '10600',
#        quote_plus('platGbCd') : '0',
#        quote_plus('bun') : '',
#        quote_plus('ji') : '',
#        quote_plus('startDate') : '',
#        quote_plus('endDate') : '',
#        quote_plus('numOfRows') : '10',
#        quote_plus('pageNo') : '1' 
#        
#    }
#    )
#
#print(queryParams)
#res = requests.get(url + queryParams)
#html = res.text
##soup = BeautifulSoup(res.content, 'html.parser')
#soup = BeautifulSoup(html, 'html.parser')
#
#data = soup.find_all('item')
#print(type(data))
#print ("\nResult:")
#print(html)
#print ("\nResult:")
#print(soup)
#    
#
##request = Request(url + queryParams)
##request.get_method = lambda: 'GET'
#response_body = urlopen(request).read()
#print(response_body)
    
 #   return render(request,'index.html', context)
    



#def detail(request,pk):
#    url = 'http://openapi.seoul.go.kr:8088/47636346646e616b3132336c5066436f/xml/ListOnePMISBizInfo/1/200'
#    requests = ul.Request(url)
#    response = ul.urlopen(requests)
#    rescode = response.getcode()
#    context = {}
#    
#    if(rescode==200):
#        responseData = response.read()
#        rD = xmltodict.parse(responseData)
#        rDJ = json.dumps(rD)
#        rDD = json.loads(rDJ)
#        gs_data = rDD['ListOnePMISBizInfo']['row']
#        gs_dict = gs_data
#        context["gs_context"] = gs_dict
#        
#        for i in gs_dict:
#            #print("*"*100,i['OFFICE_ADDR'])
#            if str(i['PJT_CD']) == str(pk):
#                context["gs_detail"] = i
#                context["gs_center"] = i
#                #print("*"*100,type(i['PJT_NAME']))
#                break
#        #print(gs_dict[0])
#        search_q = request.GET.get('q','')
#        searched_result = []
#        if search_q:
#            for i in gs_dict:
#                if i['OFFICE_ADDR'].find(search_q) > 0 or i['PJT_NAME'].find(search_q) > 0:
#                    searched_result.append(i)
#            context['gs_context'] = searched_result
#            context["gs_center"] = searched_result[0]
#        
#
#    return render(request,'index.html', context)
#    #