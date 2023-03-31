from rest_framework import serializers
from userAccounts.models import User


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'muncipality',
                  'district', 'password', 'is_active','id']
