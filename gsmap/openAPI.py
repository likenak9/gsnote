import urllib.request as ul
import requests
import xmltodict
import json
from django.shortcuts import render,redirect
#from bs4 import BeautifulSoup
#from lxml import html
#from urllib.request import urlopen,Request
# from urllib.parse import urlencode,unquote,quote_plus


url = 'http://openapi.seoul.go.kr:8088/47636346646e616b3132336c5066436f/xml/ListOnePMISBizInfo/1/100'
requests = ul.Request(url)
response = ul.urlopen(requests)
rescode = response.getcode()
context = {}
    
if(rescode==200):
    responseData = response.read()
    rD = xmltodict.parse(responseData)
    rDJ = json.dumps(rD)
    rDD = json.loads(rDJ)
    gs_data = rDD['ListOnePMISBizInfo']['row']
    gs_dict = gs_data
    context["gs_context"] = gs_dict
    print(gs_dict)
    print(context['gs_context'])
    #print(*gs_data)
    #gs_data_dict = gs_data.flatten()
    #context = dict()
    #for i in gs_data:
    #    context['gs_data'] = gs_data
    #all_post = Post.objects.all()
    #context['all_post'] = all_post
    
    #return render(request,'index.html', context)

#print(gs_dict)


#print(gs_data2)
#print(gs_data2[1]['LAT'])
#print ("\nResult:")
#print('gs_data2타입은',type(gs_data2))
#print(gs_data2.get('row'))
#
#print ("\nResult:")
#
#context = dict()
#context['gs_data3'] = gs_data2.get('row')
#print(context)
#print(type(context))
#print(len(context))
#print(context.keys())
#print(type(gs_data))
#print(type(gs_data[0]))
#print(gs_data[0])

#context = dict()
#for i in len(gs_data):
#    context['gs_data'] = gs_data['LAT']
#    print(context)
#    print(type(context))

#print(gs_data[0]['LAT'])

#print ("\nResult:")
#print(len(gs_data))
#print('gs_data타입은',type(gs_data))

#count = 0
#for l in gs_data:
#    count+= 1
#    print(str(count) +'번째 ' +'list 속 tuple의 개수:', len(l))

#print(dict(gs_data))
#print('dict로 변환', type(dict(gs_data)))
#for key, value in rDD.items():
#    print(value)
#    print(key)





    #gs_data = rDD.Objects.get('row')
    #print(gs_data)
    
#soup = BeautifulSoup(response, 'lxml-xml')
#soup = BeautifulSoup(response, 'html.parser')
#cc = xmltodict.parse(soup)
#dd = json.loads(json.dumps(cc))
#print(dd)
#myplace = soup.find_all(['lat','lng'])
#print(type(myplace))
#print(type(soup))

#print(myplace)


 #   return render(request, 'index.html',myplace)


#print(soup.prettify())
#print(soup.title)
#print(soup.find_all(['lat','lng']))
#print(soup.find_all('lng'))

#request.get_method = lambda: 'GET'
#response_body = urlopen(request).read()
#queryParams = '?' + urlencode({ quote_plus('servicekey') : 'LRz1LCEBA4jbTvkY9e9aOlDhER1Px4NShhPOt69D975W82kzo6kt5MIaI7AeqPICS%2BYjfpc3xXo8yPEP2dsLHQ%3D%3D',
#    quote_plus('sigunguCd') : '11680',
#    quote_plus('bjdongCd') : '00000',
#    quote_plus('platGbCd') : '0',
#    quote_plus('bun') : '0012',
#    quote_plus('ji') : '0012',
#    quote_plus('startDate') : '',
#    quote_plus('endDate') : '',
#    quote_plus('numOfRows') : '10',
#    quote_plus('pageNo') : '1'})

# request = urllib.request.Request(url+unquote(queryParams))
#print(queryParams)
#print ('Your Request:\n'+url+queryParams)
#request.get_method = lambda: 'GET'
#response_body = urlopen(request).read()
#print ("\nResult:")
#print (response_body)
#print ("\nDataType of Result Data:")
#print (type(response_body))

