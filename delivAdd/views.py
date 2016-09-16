from django.shortcuts import render

# Create your views here.
from delivAdd.models import Address
from delivAdd.serializer import AddressSerializer
from rest_framework import generics
from django.contrib.auth.models import User


class SnippetList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
