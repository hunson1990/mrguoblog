from django.conf.urls import url
from . import views
from . import search_view

app_name='myblog'
urlpatterns=[
    url(r'^$',views.v_index,name='index'),
    url(r'^archive/$',views.v_archive,name='archive'),
    url(r'^category/(\d+)/$',views.v_categoryDtail,name='categoryDtail'),
    url(r'^blog/(\d+)/$',views.v_blogDetail,name='blogDetail'),
    url(r'^tags/$',views.v_tags,name='tags'),
    url(r'^tags/(\d+)$',views.v_tagDetail,name='tagDetail'),
    url(r'^search/', search_view.MySearchView(), name='haystack_search'),
]

