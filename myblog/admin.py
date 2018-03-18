from django.contrib import admin
from .models import *

class blogAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['id','title','category','createTime','click_nums']
    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)
    #list_editable 设置默认可编辑字段
    list_editable = ['category', 'click_nums']
    #fk_fields 设置显示外键字段
    fk_fields = ('category',)
    # 筛选器
    list_filter =('category','tag') #过滤器
    search_fields =('title','content') #搜索字段
    #date_hierarchy = 'createTime'    # 详细时间分层筛选　

admin.site.register(blog,blogAdmin)
admin.site.register(categorys)
admin.site.register(tags)
admin.site.register(system)
admin.site.register(links)

