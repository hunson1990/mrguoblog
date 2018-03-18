"""mrguoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from mrguoblog.settings import STATIC_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('myblog.urls')),
    url(r'^spider/',include('articleSpider.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
]

# 配置全局404页面
hander404 = 'myblog.views.page_not_found'

# 配置全局505页面
hander505 = 'myblog.views.page_errors'



#添加静态文件的访问处理函数
#url(r'^static/(?P<path>.*)/$', serve, {'document_root': STATIC_ROOT}),

