from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import requests

from django.core.cache import cache

#Navigate to 127.0.0.1:8000/metar/ping to run this method.
def demo(request):
    responseData = {'data':'pong'}
    return JsonResponse(responseData) #returns JSON response

'''
Method : preprocess
input : response
output : Normalized params,values in dictionary format
'''
def preprocess(res):
    s = str(res)
    s = s.split('\\n')
    print(len(s))
    s[0] = s[0].replace('b','')
    s[0] = s[0].replace('"','')
    s.remove(s[-1])
    for i in range(len(s)):
        s[i] = s[i].replace("'",'')
    params = normalize(s)
    if(params == 0):
        return False
    return params


'''
Method : normalize
input : list of the params and values
output : Normalized params,values in dictionary format
'''
def normalize(cleanedList):
    try:
        params = {}
        if(cleanedList[0] == 'Station name not available'):params['station'] = 'Station Name Unavailable'
        else:params['station'] = cleanedList[0]
        params['latest_observation'] = cleanedList[1]
        for i in range(2,len(cleanedList)):
            para = cleanedList[i].split(':',1)
            params[para[0]] = para[1]
        return params
    except:
        return False

'''
Method : fetch_data
input : request
output : JSONResponse as output
'''
def fetch_data(request):
    id = request.GET.get('scode')
    cache_status = request.GET.get('nocache')
    if(cache.get(id) and cache_status != '1'):
        data = cache.get(id)
    else:
        name = 'https://tgftp.nws.noaa.gov/data/observations/metar/decoded/'+id+'.TXT'
        res = requests.get(name)
        res = res.content
        params = preprocess(res)
        if(not params):
            return HttpResponse('<h1>Please Enter Valid Details!</h1>')
        data = {'data':params}
        cache.set(id,data)
    return JsonResponse(data)