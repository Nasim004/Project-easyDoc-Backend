from rest_framework import serializers
from userAccounts.models import User,Booking


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'muncipality',
                  'district', 'password', 'is_active','id']

class Booking_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'