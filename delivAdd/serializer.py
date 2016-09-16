#-*- coding:utf-8 –*-

from rest_framework import serializers

from delivADD import Address


class AddressSerializer(serializers.ModelSerializer):
    """docstring for ClassName"""
    class Meta:
        model=Address
        fields=('id','recipent_name','cellphone','province_name','city','street','postal_code','address_tag',)



