#from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from blog.models import Account
from .serializer import AccountSerializer


# Create your views here.
class AccountList(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer