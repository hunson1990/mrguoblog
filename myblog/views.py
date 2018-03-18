from django.shortcuts import render
from .models import *
from pure_pagination import PageNotAnInteger, Paginator
from django.views.decorators.cache import cache_page


def v_common():
    categorysObj = categorys.objects.all()

    #博客链接
    linksObj=links.objects.all()

    #博客正副标题/关键字/描述，系统配置
    systemObj=system.objects.get(id=1)
    title=systemObj.title
    subtitle=systemObj.subtitle
    keywords=systemObj.keywords
    description=systemObj.description
    #日志/分类/标签数量统计
    blogNum=systemObj.blogNum
    categoryNum=systemObj.categoryNum
    tagNum=systemObj.tagNum

    context={
        'title': title,
        'subtitle':subtitle,
        'keywords':keywords,
        'description':description,

        'blogCount':blogNum,
        'categoryCount':categoryNum,
        'tagCount': tagNum,

        'categorys':categorysObj,
        'links': linksObj,
    }
    return  context

@cache_page(60*2)
def v_index(request):
    '''首页'''
    blogs=blog.objects.all().order_by('-id')

    #分页
    try:
        page=request.GET.get('page',1)
    except PageNotAnInteger:
        page=1
    p = Paginator(blogs, 5, request=request)  # 5为每页展示的博客数目
    blogs = p.page(page)

    context={
        'blogs':blogs,
    }
    contextComm=v_common()
    context=dict(context, **contextComm)
    return render(request,'myblog/index.html',context)

@cache_page(60*2)
def v_tags(request):
    '''标签'''
    Tags=tags.objects.all()
    context={
        'subTitle':'标签',
        'tagsCount': Tags.count(),
        'tags':Tags,
    }
    contextComm=v_common()
    context=dict(context, **contextComm)
    return render(request, 'myblog/tags.html',context)

@cache_page(60*2)
def v_tagDetail(request,tagId):
    tag=tags.objects.get(id=tagId)
    blogs=tag.blog_set.all()

    #分页
    try:
        page=request.GET.get('page',1)
    except PageNotAnInteger:
        page=1
    p = Paginator(blogs, 5, request=request)  # 5为每页展示的博客数目
    blogs = p.page(page)


    context={
        'tag':tag,
        'subTitle': tag.name,
        'blogs':blogs,
    }
    contextComm=v_common()
    context=dict(context, **contextComm)
    return render(request, 'myblog/tag_detail.html',context)


@cache_page(60*2)
def v_archive(request):
    '''归档'''
    blogs = blog.objects.all().order_by('-id')
    blogsNum=blogs.count()
    #分页
    try:
        page=request.GET.get('page',1)
    except PageNotAnInteger:
        page=1
    p = Paginator(blogs, 5, request=request)  # 5为每页展示的博客数目
    blogs = p.page(page)

    context={
        'subTitle': '归档',
        'blogs':blogs,
        'blogsCount':blogsNum,
    }
    contextComm=v_common()
    context=dict(context, **contextComm)
    return render(request, 'myblog/archive.html',context)


@cache_page(60*2)
def v_categoryDtail(request,categoryId):
    '''
    分类详细页面
    '''
    category=categorys.objects.get(id=categoryId)
    blogs=category.blog_set.all()

    #分页
    try:
        page=request.GET.get('page',1)
    except PageNotAnInteger:
        page=1
    p = Paginator(blogs, 5, request=request)  # 5为每页展示的博客数目
    blogs = p.page(page)


    context={
        'category':category,
        'subTitle': category.name,
        'blogs':blogs,
    }
    contextComm=v_common()
    context=dict(context, **contextComm)
    return render(request, 'myblog/category_detail.html',context)


def v_search(request):
    '''搜索'''
    return render(request, 'myblog/search.html')

@cache_page(60*2)
def v_blogDetail(request,blogId):
    '''博客详情'''
    blogMsg=blog.objects.get(id=blogId)
    blogTags=blogMsg.tag.all()
    #博客文章点击数增加1
    blogMsg.click_nums=blogMsg.click_nums+1
    blogMsg.save()
    #上 下篇文章
    blog_pre=blog.objects.filter(id__gt=blogId).order_by('id')
    if blog_pre:
        blog_pre=blog_pre[0]
    else:
        blog_pre=False

    blog_next=blog.objects.filter(id__lt=blogId).order_by('-id')
    if blog_next:
        blog_next=blog_next[0]
    else:
        blog_next=False


    context={
        'blog':blogMsg,
        'blogTags':blogTags,
        'blog_pre':blog_pre,
        'blog_next':blog_next,
    }
    contextComm=v_common()
    context=dict(context, **contextComm)
    return render(request, 'myblog/blog_detail.html',context)


#配置404 500错误页面
def page_not_found(request):
    return render(request, '404.html')

def page_errors(request):
    return render(request, '500.html')





