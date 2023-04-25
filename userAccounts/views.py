from rest_framework.response import Response    
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from userAccounts.serializers import User_Serializer, Booking_Serializer
from userAccounts.models import User, Booking
import jwt
from django.contrib.auth.hashers import make_password, check_password
import json
import base64
import random
from hospitalAccounts.models import Hospital, Doctor
from hospitalAccounts.serializers import Hospital_Serializer, Doctor_serializer


class Sign_up(APIView):

    def post(self, request):

        try:
            name = request.data['name']
            email = request.data['email']
            phone = request.data['phone']
            password = make_password(request.data['password'])
        except:
            return Response({'status': 'Please Provide The Details(name,email,phone,muncipality,district,password)'})

        if len(name) < 3:
            return Response({'status': 'Name should be minimum of 3 letters'})
        if len(password) < 5:
            return Response({'status': 'Password should be minimum of 5'})

        check_user = User.objects.all()

        for i in check_user:
            if i.email == email:
                return Response({'status': 'Email is already Exist'})
            elif i.phone == phone:
                return Response({'status': 'Phone Number is already Exist'})

        user = User.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password,
        )
        user.save()

        return Response({'status': 'Success'})


class Login(APIView):
    def post(self, request):

        try:
            email = request.data['email']
            password = str(request.data['password'])
        except:
            return Response({'status': 'Please Provide details(email,password)'})

        user = User.objects.all()
        status = 'None'

        for i in user:
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
                        {'status': 'Success', 'payload': enpayload, 'jwt': jwt_token, 'role': 'user', 'id': i.id})
                    return response
                else:
                    status = 'Wrong Password'
                    break
            else:
                status = 'Email is not found'

        return Response({'status': status})


class Logout(APIView):
    def get(self, request):
        response = Response({'status': 'success'})
        response.delete_cookie('jwt')
        return response


@api_view(['POST'])
def verifyToken(request):
    token = request.data.get('token')
    decoded = jwt.decode(token, 'secret', algorithms='HS256')
    # Decode  payload
    decoded_bytes = base64.b64decode(decoded['payload'])
    #  byte string to unicode string
    decoded_str = decoded_bytes.decode('utf-8')
    decoded1 = json.loads(decoded_str)  # Parse JSON string as dictionary
    user = User.objects.get(email=decoded1.get('email'))

    if user:
        return Response({'username': user.name, 'id': user.id})
    else:
        return Response({'status': 'Token InValid'})


@api_view(['GET'])
def myProfile(request, id):
    user = User.objects.filter(id=id)
    serializer = User_Serializer(user, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
def profileUpdate(request, id):
    try:
        name = request.data['name']
        phone = request.data['phone']
        email = request.data['email']
    except:
        return Response('Please provide all details')

    user = User.objects.get(id=id)

    # if User.objects.filter(email=email).exists():
    #     return Response("Email is already taken")
    # if User.objects.filter(phone=phone).exists():
    #     return Response("Phone number is already taken")

    user.name = name
    user.email = email
    user.phone = phone
    user.save()

    return Response("Profile Updated Successfully")


@api_view(["PUT"])
def change_password(request, id):
    try:
        old = request.data['oldpassword']
        new = request.data['newpassword']
    except:
        return Response('Please Fill All Details')
    user = User.objects.get(id=id)
    if check_password(old, user.password):
        user.password = make_password(new)
        user.save()
        return Response("Password Updated")
    return Response("Old Password Is Wrong")


@api_view(["GET"])
def randomHospital(request):
    hospitals = Hospital.objects.filter(is_approved=True)
    hospital = random.sample(list(hospitals), 4)
    serializer = Hospital_Serializer(hospital, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def Hospital_details(request):
    hospital = Hospital.objects.filter(is_approved=True)
    serializer = Hospital_Serializer(hospital, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def Hospital_detail(request, id):
    hospital = Hospital.objects.get(id=id)
    serializer = Hospital_Serializer(hospital)
    return Response(serializer.data)


@api_view(["GET"])
def Doctor_detail(request, id):
    doctor = Doctor.objects.filter(hospital_id=id)
    serializer = Doctor_serializer(doctor, many=True)
    return Response(serializer.data)


class Bookings(APIView):
    def post(self, request):
        try:
            name = request.data['name']
            age = request.data['age']
            phone = request.data['phone']
            token = request.data['bookingtoken']
            date = request.data['date']
            address = request.data['address']
            user_id = request.data['user_id']
            doctor_id = request.data['id']

        except:
            return Response({"status": "Please give all details"})

        booking = Booking.objects.create(
            name=name,
            age=age,
            phone=phone,
            token=token,
            date=date,
            address=address,
            user_id=user_id,
            doctor_id=doctor_id,
        )
        booking.save()

        return Response({'staus': "Success"})




@api_view(["GET"])
def tokens(request,id):
    tokens = Doctor.objects.filter(id=id).values('tokens')
    # serializer = Doctor_serializer(tokens,many=True)
    # return Response(serializer.data)
    return Response(tokens)




