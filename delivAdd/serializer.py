#-*- coding:utf-8 –*-

from rest_framework import serializers

from delivAdd.models import Address


class AddressSerializer(serializers.ModelSerializer):
    """docstring for ClassName"""
    class Meta:
        model=Address
        fields=('recipent_name','cellphone','province','city','street','postal_code','address_tag')



