from django.db import models
from tinymce.models import HTMLField


# Create your models here.
from django.utils import timezone

class categorys(models.Model):
    '''博客分类'''
    name=models.CharField(verbose_name='博客分类',max_length=20)
    class Meta:
        verbose_name='博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class tags(models.Model):
    '''博客标签'''
    name=models.CharField(verbose_name='博客标签',max_length=20)
    class Meta:
        verbose_name='博客标签'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name



class blog(models.Model):
    '''我的博客'''
    title=models.CharField(verbose_name='博客标题',max_length=100)
    content=HTMLField('博客内容',null=True)
    createTime=models.DateTimeField(verbose_name='创建时间',default=timezone.now)
    modifyTime=models.DateTimeField(verbose_name='修改时间',auto_now=True)
    click_nums=models.IntegerField(verbose_name='点击量',default=0)
    category=models.ForeignKey(categorys,verbose_name='博客分类',on_delete=models.CASCADE)
    tag=models.ManyToManyField(tags,verbose_name='博客标签')

    class Meta:
        verbose_name='我的博客'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title


'''
#博客评论model 关闭
class comment(models.Model):
    name=models.CharField(verbose_name='姓名',max_length=20,default='译名')
    content=models.CharField(verbose_name='内容',max_length=300)
    createTime=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    blog=models.ForeignKey(blog,verbose_name='博客')

    class Meta:
        verbose_name='博客评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:10]

'''

class links(models.Model):
    '''友情链接'''
    name=models.CharField(verbose_name='链接名称',max_length=20)
    url=models.CharField(verbose_name='链接',max_length=100)
    class Meta:
        verbose_name='友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class system(models.Model):
    '''博客系统设置'''
    title=models.CharField(verbose_name='博客标题',max_length=40)
    subtitle=models.CharField(verbose_name='博客副标题',max_length=80)
    keywords=models.CharField(verbose_name='关键字',max_length=100)
    description=models.CharField(verbose_name='描述',max_length=300)
    '''日志,分类,标签的统计'''
    blogNum=models.IntegerField(verbose_name='日志数量',default=0)
    categoryNum=models.IntegerField(verbose_name='分类数量',default=0)
    tagNum=models.IntegerField(verbose_name='标签数',default=0)


    class Meta:
        verbose_name='博客系统设置'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title





