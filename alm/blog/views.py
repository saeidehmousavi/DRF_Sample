from django.shortcuts import render
from django.views.generic import ListView
from .models import Account

# Create your views here.
class AccountList(ListView):
    def get_queryset(self):
        return Account.objects.filter(status=True)
