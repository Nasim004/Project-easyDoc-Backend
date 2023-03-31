from rest_framework import serializers
from hospitalAccounts.models import Hospital,Department,Doctor


class Hospital_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id','name', 'username', 'admin_name', 'admin_position',
                  'phone', 'email', 'muncipality', 'district', 'password','is_approved','description']



class Department_serializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name']



class Doctor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','name','experience','is_available','tokens','department_id','hospital_id']


        


        
