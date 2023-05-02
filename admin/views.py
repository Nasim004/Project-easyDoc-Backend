from django.shortcuts import render
from rest_framework.response import Response
from userAccounts.models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import jwt
from hospitalAccounts.models import Hospital, Department,Doctor
import json
import base64
from hospitalAccounts.serializers import Hospital_Serializer, Department_serializer
from userAccounts.serializers import User_Serializer
from django.contrib.auth.hashers import check_password


class Login(APIView):

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']

        except:
            return Response({'status': 'Please Give All Details'})

        admin = User.objects.all()
        status = 'None'

        for i in admin:
            if i.is_superuser:
                if i.email == email:
                    if check_password(password, i.password):
                        payload = {
                            'email': email,
                            'password': password
                        }
                        enpayload = base64.b64encode(json.dumps(
                            payload).encode('utf-8')).decode('utf-8')
                        jwt_token = jwt.encode(
                            {'payload': enpayload}, 'secret', algorithm='HS256')
                        response = Response(
                            {'status': 'Success', 'payload': payload, 'jwt': jwt_token, 'role': 'admin'})

                        return response

                    else:
                        status = 'Wrong Password'
                        break
                else:
                    status = 'Wrong Username'
            else:
                status = 'Not A Admin Account'
        return Response({'status': status})


@api_view(['GET'])
def Hospital_details(request):
    hospital = Hospital.objects.all().order_by('id')
    serializer = Hospital_Serializer(hospital, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def Hospital_approval(request, id):
    hospital = Hospital.objects.get(id=id)
    if hospital.is_approved:
        hospital.is_approved = False
        hospital.save()
    else:
        hospital.is_approved = True
        hospital.save()
    return Response("Updated")


@api_view(['DELETE'])
def Hospital_delete(request, id):
    hospital = Hospital.objects.get(id=id)
    hospital.delete()
    return Response("Hospital Deleted")


class Department_add(APIView):
    def post(self, request):
        try:
            name = request.data['name']
        except:
            return Response({'status': 'Please give all details'})

        if len(name) < 3:
            return Response({'status': 'Name should be minimum 3 letter'})

        check_department = Department.objects.all()

        for i in check_department:
            if i.name == name:
                return Response({'status': 'Department already Exist'})

        department = Department.objects.create(
            name=name,
        )
        department.save()
        return Response({'status': 'Success'})


@api_view(['GET'])
def Department_details(request):
    department = Department.objects.all().order_by('id')
    serializer = Department_serializer(department, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def Department_delete(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return Response("Department Deleted")


@api_view(['GET'])
def User_details(request):
    user = User.objects.all().order_by('id')
    serializer = User_Serializer(user, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def Block_user(request, id):
    user = User.objects.get(id=id)
    if user.is_active:
        user.is_active = False
        user.save()
    else:
        user.is_active = True
        user.save()
    return Response("Updated")


@api_view(['GET'])
def Counts(request):
    hospital = Hospital.objects.filter(is_approved=True).count()
    departments = Department.objects.all().count()
    users = User.objects.all().count()
    doctors = Doctor.objects.all().count()
    return Response({'users':users,'hospital':hospital,'departments':departments,'doctors':doctors})



@api_view(['GET'])
def departments(request,id):
    department = Department.objects.get(id=id)
    serializer = Department_serializer(department,many=False)
    return Response(serializer.data)
    
