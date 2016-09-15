#-*-coding:utf-8-*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ChinaProvinces(models.Model):

    name = models.CharField(pgettext_lazy('china provinces', 'name'),max_length=12)

    uq_id = models.CharField(('china provinces', 'uq_id'),max_length=6, unique=True)

    enable = models.BooleanField(default="True")

    sort = models.SmallIntegerField('sort', default=0)

	def __str__(self):

	    return self.name



class ChinaCity(models.Model):

    //由於前面提到的直轄市並不隸屬於任何省,所以要設定null=True

    province = models.ForeignKey(ChinaProvinces, related_name='province', blank=True, null=True)

    name = models.CharField(pgettext_lazy('china city', 'name'),max_length=12)

    uq_id = models.CharField(pgettext_lazy('china city', 'uq_id'),max_length=6, unique=True)

    enable = models.BooleanField(default="True")

    is_municipality = models.BooleanField(default=False)

    sort = models.SmallIntegerField('sort', default=0)

	def __str__(self):

        return self.name



class ChinaDistrict(models.Model):

    city = models.ForeignKey(ChinaCity, related_name='city',)

    name = models.CharField(pgettext_lazy('china district', 'name'),max_length=12)

    uq_id = models.CharField(pgettext_lazy('china district', 'uq_id'),max_length=6, unique=True)

    enable = models.BooleanField(default="True")

    sort = models.SmallIntegerField('sort', default=0)

    def __str__(self):

        return self.name


