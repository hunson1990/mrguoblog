from django.conf.urls import url
from .import views

app_name='articleSpider'
urlpatterns=[
    url(r'^get_ip/$', views.get_ip_view, name='get_ip'),
    url(r'^scrapyd/$', views.process_scrapyd_view, name='process_scrapyd'),
]

