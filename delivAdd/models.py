#-*-coding:utf-8-*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Province(models.Model):
    """docstring for p"""
    iso_code = models.CharField(max_length = 3, primary_key = True)
    province_name = models.CharField(verbose_name="省",max_length = 7, blank = False)

class City(models.Model):
	"""docstring for city"""
	id = models.CharField(max_length =13, primary_key = True)

	city_name = models.CharField(max_length = 55, blank = False)
	province = models.ForeignKey(Province,verbose_name='城市',blank = False,to_field='iso_code')


class Street(models.Model):
	"""docstring for street"""
	id = models.CharField(max_length =13, primary_key = True)

	street_name = models.CharField(max_length = 55, blank = False)
	city = models.ForeignKey(City,verbose_name='街道',blank = False,to_field='id')


class Address(models.Model):
    recipent_name=models.CharField("姓名", max_length = 20,blank = False)
    cellphone=models.CharField("电话号码", max_length = 11,blank = False)
    postal_code = models.CharField("邮政编号", max_length = 10)
    address_tag = models.CharField("地址标签", max_length = 10)
    province = models.ForeignKey(Province,verbose_name='省',to_field='iso_code')
    city = models.ForeignKey(City,verbose_name='城市',blank = False,to_field='id')
    street = models.ForeignKey(Street,verbose_name='街道',blank = False,to_field='id')
