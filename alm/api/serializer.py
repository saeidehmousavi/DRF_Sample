from  rest_framework import serializers
from blog.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        #fields = ['id', 'account', 'slug', 'title', 'content', 'publish', 'status']
        #excluded =  ['user']
        