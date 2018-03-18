# coding=utf-8

from haystack.views import SearchView
from pure_pagination import PageNotAnInteger, Paginator
from django.http import HttpResponse

from mrguoblog.settings import HAYSTACK_SEARCH_RESULTS_PER_PAGE
from .views import *

class MySearchView(SearchView):
    '''
    def extra_context(self):  # 重载extra_context来添加额外的context内容
        context = super(MySearchView,self).extra_context()
        context['title'] = '搜索'
        return context
    '''

    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        # 博客、标签、分类数目统计
        contextComm = v_common()
        context2 = {
            'subTitle':'搜索'
        }
        context = dict(context, **contextComm, **context2)
        return context

    def build_page(self):
        #分页重写
        super(MySearchView, self).extra_context()

        try:
            page_no = int(self.request.GET.get('page', 1))
        except PageNotAnInteger:
            raise HttpResponse("Not a valid number for page.")

        if page_no < 1:
            raise HttpResponse("Pages should be 1 or greater.")


        paginator = Paginator(self.results, HAYSTACK_SEARCH_RESULTS_PER_PAGE,request=self.request)
        page = paginator.page(page_no)

        return (paginator, page)