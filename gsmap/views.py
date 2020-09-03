import requests
import xmltodict
import json
#import numpy as np
import urllib.request as ul
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.db.models import Q





User = get_user_model()
# Create your views here.
def index(request):
    url = 'http://openapi.seoul.go.kr:8088/47636346646e616b3132336c5066436f/xml/ListOnePMISBizInfo/1/200'
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
        context["gs_center"] = gs_dict[0]
     
        search_q = request.GET.get('q','')
        searched_result = []
        if search_q:
            for i in gs_dict:
                if i['OFFICE_ADDR'].find(search_q) > 0 or i['PJT_NAME'].find(search_q) > 0:
                    searched_result.append(i)
            context['gs_context'] = searched_result
            context["gs_center"] = searched_result[0]
            
    return render(request,'index.html', context)
    

#https://data.seoul.go.kr/dataList/OA-2540/A/1/datasetView.do;jsessionid=7822E40685C0DB204AE6D1CF62BFE6BD.new_portal-svr-11

#<PJT_CD>043012061101</PJT_CD>
#사업명 <PJT_NAME>신림~봉천터널 도로건설공사(1공구)</PJT_NAME>
#준공여부구분<PJT_FIN_YN>1</PJT_FIN_YN>
#준공여부<PJT_FIN_YN_NM>진행 </PJT_FIN_YN_NM>
#<PLAN_RT>18.93</PLAN_RT>
#<REAL_RT>18.93</REAL_RT>
#<PER_RT>100</PER_RT>
#<BASIC_DT>20200823</BASIC_DT>
#<DT1>4836</DT1>
#<DT2>3612</DT2>
#<DT3>1223</DT3>
#<TOT_CNTRT_AMT>2,237.63</TOT_CNTRT_AMT>
#사업비(억원) <TOT_PJT_AMT>3,326.13</TOT_PJT_AMT>
#<DU_DATE>2010-10-05 ~ 2023-12-31</DU_DATE>
#<OFFICE_ADDR>관악구 신림동 1667-9 ~ 신림동 393-1</OFFICE_ADDR>
#<LAT>37.47969374474193</LAT>
#<LNG>126.90099423602912</LNG>
#<USER_1>이상근</USER_1>
#<USER_2>유기상(책임건설사업관리자)</USER_2>
#<USER_3>박용수(현장대리인)</USER_3>
#<ORG_1>도시기반시설본부</ORG_1>
#<ORG_2>주식회사 동일기술공사</ORG_2>
#<ORG_3>두산건설 주식회사</ORG_3>
#사업규모<PJT_SCALE> - 도로건설 연장 3.1km(폭원 왕복 4차로) (터널 1,720m 지하차도 877m, 공기정화시설 ...</PJT_SCALE>
#<RTSP_ADDR/>
#<CNRT_ADDR>http://cis.seoul.go.kr/TotalAlimi/PopInfo.action?cmd=info2&pjt_cd=043012061101</CNRT_ADDR>
#<BILLPAY_ADDR>http://cis.seoul.go.kr/TotalAlimi/PopInfo.action?cmd=info6&pjt_cd=043012061101</BILLPAY_ADDR>
#<AIR_VIEW_IMG>http://pmis.eseoul.go.kr/data/edms/201202/1202141844989462.edm</AIR_VIEW_IMG>
#<ALIMI_ADDR>http://cis.seoul.go.kr/TotalAlimi/PopInfo.action?cmd=info1&pjt_cd=043012061101</ALIMI_ADDR>
#

def detail(request,pk):
    url = 'http://openapi.seoul.go.kr:8088/47636346646e616b3132336c5066436f/xml/ListOnePMISBizInfo/1/200'
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
        
        for i in gs_dict:
            #print("*"*100,i['OFFICE_ADDR'])
            if str(i['PJT_CD']) == str(pk):
                context["gs_detail"] = i
                context["gs_center"] = i
                #print("*"*100,type(i['PJT_NAME']))
                break
        #print(gs_dict[0])
        search_q = request.GET.get('q','')
        searched_result = []
        if search_q:
            for i in gs_dict:
                if i['OFFICE_ADDR'].find(search_q) > 0 or i['PJT_NAME'].find(search_q) > 0:
                    searched_result.append(i)
            context['gs_context'] = searched_result
            context["gs_center"] = searched_result[0]
        

    return render(request,'index.html', context)
    
#from django.http import HttpResponseRedirect
#def like(request,pk):
#    context = {}
#
#    if context['gs_like'].find(pk) > 0 :
#        del(context['gs_like'])
#        print("이 글의 좋아요를 취소했습니다.")
#    else:
#        context['gs_like'] =  pk
#        print("이 글을 좋아합니다")
#        
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#    
