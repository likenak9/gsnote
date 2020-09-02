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
    #print(*gs_data)
    #gs_data_dict = gs_data.flatten()
    #context = dict()
    #for i in gs_data:
    #    context['gs_data'] = gs_data
    #all_post = Post.objects.all()
    #context['all_post'] = all_post
    
    return render(request,'index.html', context)
    
    
    def map
    
# 'PJT_CD': '6042019082998'
# 'PJT_NAME': '금호로 확장 통신공사(정보통신)'
# 'PJT_FIN_YN': '1'
# 'PJT_FIN_YN_NM': '진행'
# 'PLAN_RT': '73.26'
# 'REAL_RT': '73.26'
# 'PER_RT': '100'
# 'BASIC_DT': None
# 'DT1': '476'
# 'DT2': '348'
# 'DT3': '127'
# 'TOT_CNTRT_AMT': '.91'
# 'TOT_PJT_AMT': '.91'
# 'DU_DATE': '2019-09-02 ~ 2020-12-20'
# 'OFFICE_ADDR': '서울 성동구 금호로 일대'
# 'LAT': '37.55165599975385'
# 'LNG': '127.02547629571266',
# 'USER_1': '-'
# 'USER_2': '-'
# 'USER_3': '-'
# 'ORG_1': '-'
# 'ORG_2': '-'
# 'ORG_3': '-'
# 'PJT_SCALE': '-'
# 'RTSP_ADDR': None
# 'CNRT_ADDR': None
# 'BILLPAY_ADDR': None
# 'AIR_VIEW_IMG': None

    
def detail(request):
#    context = dict()
 #   detail_post = Post.objects.get(id = post_id)
  #  context['detail_post'] = detail_post
    return render(request,'detail.html')
    
    