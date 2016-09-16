#-*-coding:utf-8-*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Address(models.Model):
    recipent_name=models.CharField("姓名", max_length = 20，blank = False)
    cellphone=models.CharField("电话号码", max_length = 11，blank = False)
    province_name = models.CharField(verbose_name="省",max_length = 7, blank = False)
    city = models.ForeignKey(province_name,verbose_name='城市',blank = False)
    street = models.ForeignKey(city,verbose_name='街道',blank = False)
    postal_code = models.CharField("邮政编号", max_length = 10)
    address_tag = models.CharField("地质标签", max_length = 10)
