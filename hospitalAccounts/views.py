from rest_framework.response import Response
from rest_framework.views import APIView
from .authentications import check_user
from rest_framework.decorators import api_view
import jwt
from hospitalAccounts.models import Hospital, Department, Doctor
from hospitalAccounts.serializers import Doctor_serializer, Department_serializer 
from userAccounts.serializers import Booking_Serializer
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from userAccounts.models import Booking

class Sign_up(APIView):

    def post(self, request):

        try:
            name = request.data['name']
            username = request.data['username']
            admin_name = request.data['admin_name']
            admin_position = request.data['admin_position']
            phone = request.data['phone']
            email = request.data['email']
            muncipality = request.data['muncipality']
            district = request.data['district']
            description = request.data['description']
            password = request.data['password']

        except:
            return Response({'status': 'Please give all details'})

        check_hospital = Hospital.objects.all()

        for i in check_hospital:
            if i.email == email:
                return Response({'status': 'Email is already Exist'})
            elif i.username == username:
                return Response({'status': 'Username is already Exist'})
            elif i.phone == phone:
                return Response({'status': 'Phone Number is already Exist'})

        hospital = Hospital.objects.create(
            name=name,
            username=username,
            admin_name=admin_name,
            admin_position=admin_position,
            phone=phone,
            email=email,
            muncipality=muncipality,
            district=district,
            description=description,
            password=password,
        )

        hospital.save()
        send_mail('New Hospital Account Created',
        'Hello Admin, a new hospital is registered. The hospital name is {}.'.format(name),
        'settings.EMAIL_HOST_USER',
        ['nasimmohammed260@gmail.com'],
        fail_silently=False
        )

        # send_email(name)


        return Response({'status': 'Success'})


class Login(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
        except:
            return Response('Please give all details')
        user = Hospital.objects.filter(username=username).first()
        if user is not None:
            id = user.id
            response = check_user(user, password, username, id)
            if response is not None:
                return response
        return Response('Authentication Failed')


class Doctor_add(APIView):
    def post(self, request):

        name = request.data['name']
        experience = request.data['experience']
        department_id = request.data['department_id']
        department = Department.objects.get(id=department_id)
        hospital_id = request.data['hospital_id']
        hospital = Hospital.objects.get(id=hospital_id)
        fee = request.data['fee']
        tokens = request.data['tokens']

        token = [int(x) for x in tokens.split(',')]

        doctor = Doctor.objects.create(
            name=name,
            experience=experience,
            hospital=hospital,
            department=department,
            fee=fee,
            tokens=token,

        )
        doctor.save()
        return Response("Doctor Created")


@api_view(['GET'])
def Doctor_details(request, hospital_id):
    doctors = Doctor.objects.filter(hospital_id=hospital_id)
    serializer = Doctor_serializer(doctors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Counts(request, id):
    doctors = Doctor.objects.filter(hospital_id=id).count()
    return Response({'doctors': doctors})


@api_view(['PUT'])
def Doctor_availablity(request, id):
    doctor = Doctor.objects.get(id=id)
    if doctor.is_available:
        doctor.is_available = False
        doctor.save()
    else:
        doctor.is_available = True
        doctor.save()
    return Response(" Availablity Updated")




@api_view(['GET'])
def appointments(request,id):
    appointment = Booking.objects.filter(hospital_id=id)
    serializer = Booking_Serializer(appointment,many=True)
    return Response(serializer.data)
