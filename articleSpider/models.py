from django.db import models

# Create your models here.
class ips(models.Model):
    '''免费ip的API'''
    ip=models.CharField(verbose_name='ip地址',max_length=20,default='0.0.0.0')
    ip_hashid=models.CharField(verbose_name='ip哈希值',max_length=40,primary_key=True)

    class Meta:
        app_label='articleSpider'
        verbose_name='ip_api'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip



