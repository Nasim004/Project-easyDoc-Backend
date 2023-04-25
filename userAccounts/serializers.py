from rest_framework import serializers
from userAccounts.models import User,Booking


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Booking_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'