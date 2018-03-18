from django.shortcuts import render
from django.http import JsonResponse
from .models import ips
from myblog.views import v_common
import random
import requests
import json
# Create your views here.
def get_ip_view(request):
    ipCount=ips.objects.count()
    ip_index=random.randint(0,ipCount)
    ipObj = ips.objects.all()[ip_index]
    content={
        'ip':ipObj.ip,
        'ip_hashid':ipObj.ip_hashid,
    }
    return  JsonResponse(data=content)




def process_scrapyd_view(request):

    url_articleSpider='http://127.0.0.1:6800/listspiders.json?project=articleSpider'

    def get_spiders(url):
        r=requests.get(url)
        r_json=json.loads(r.text)
        spiders=r_json['spiders']
        return spiders

    articleSpiders=get_spiders(url_articleSpider)
    #articleSpider项目里面的爬虫


    context={
        'articleSpiders':articleSpiders
    }
    contextComm=v_common()
    context=dict(context, **contextComm)
    return render(request, 'articleSpider/scrapyd.html', context)
