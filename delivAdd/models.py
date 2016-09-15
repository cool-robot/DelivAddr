#-*-coding:utf-8-*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Address(models.Model):
	RecipientsName=models.CharField(('china provinces', 'name'),max_length=12)