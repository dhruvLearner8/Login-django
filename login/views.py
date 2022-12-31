from django.shortcuts import render, redirect
from .serializers import AllUserSerializers
from django.contrib import messages
from .models import User_details
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password

# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = [ "full_name", "email", "password","age"]

# #Serializer to Register User
# class RegisterSerializer(serializers.ModelSerializer):
#   email = serializers.EmailField(
#     required=True,
#     validators=[UniqueValidator(queryset=User.objects.all())]
#   )
#   password = serializers.CharField(
#     write_only=True, required=True, validators=[validate_password])
#   password2 = serializers.CharField(write_only=True, required=True)
#   class Meta:
#     model = User
#     fields = ('email', 'password', 'password2',
#          'full_name', 'age')
#     extra_kwargs = {
#       'email': {'required': True},
#       'password': {'required': True}
#     }
#   def validate(self, attrs):
#     if attrs['password'] != attrs['password2']:
#       raise serializers.ValidationError(
#         {"password": "Password fields didn't match."})
#     return attrs
#   def create(self, validated_data):
#     user = User.objects.create(
#       full_name=validated_data['full_name'],
#       email=validated_data['email'],
#       age=validated_data['age'],
#     #   last_nam=validated_data['last_name']
#     )
#     user.set_password(validated_data['password'])
#     user.save()
#     return user


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def home(request):
    return render(request,"home.html")

# @api_view(['POST',])
# def register(request):
#     if request.method=='POST':
#         serializer= RegistrationSealizers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         if serializer.is_valid():
#             User=serializer.save()
#             data['response']="successfully created user"
#             data['email']=User.email
#         else:
#             data=serializer.errors
#         return Response(data)

def register(request):
    if request.method=='POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        age=request.POST['age']
        dob=request.POST['dob']

        
        if User_details.objects.filter(email=email).exists():
            messages.info(request,'Username Already taken')
            print('username taken')
            return redirect('register')
        
        if pass1!=pass2:
            messages.info(request,'Password not matching!!')
            return redirect('register')
        Lower=False
        Upper=False
        num=False
        
        if (pass1==pass2 and len(pass1)>=8):
            for i in pass1:
                if ord(i)>=65 and ord(i)<=91:
                    Upper=True
                    break
            for i in pass1:
                if ord(i)>=97 and ord(i)<=123:
                    Lower=True
                    break
            for i in pass1:
               # print(ord(i))
                if (ord(i)<65 or ord(i)>91) :
                    if (ord(i)<97 or ord(i)>123):
                        
                        num=True
                        break  
            
            #print(num,Upper,Lower)
            if (Lower is True and Upper is True and num is True):
                print(num)
                obj1=User_details()
                obj1.full_name=full_name
                obj1.email=email
                obj1.password=pass1
                obj1.age=age
                obj1.dob=dob
                obj1.save()
                return redirect('login')
            else:
                messages.info(request,'please check validation of your password')
                return redirect('register')
        else:
            messages.info(request,'Password must be atleast 8 character long')
            return redirect('register')


    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        pass1=request.POST['password']
        email=request.POST['email']
        if User_details.objects.filter(email=email).exists():
            obj1=User_details.objects.get(email=email)
            if obj1.password==pass1:
                request.session['user']=obj1.id
                return redirect('home')
            else:
                messages.info(request,'Wrong Password')
                return redirect('login')
        else:
            messages.info(request,'wrong email entered')


    else:
        return render(request,'login.html')

def home(request):
    if 'user' in request.session.keys():
        user=User_details.objects.get(id=int(request.session['user']))
        return render(request,'home.html',{'user':user})
    else:
        return redirect('login')




@api_view(['GET',])
def admin_users(request):
    if 'user' in request.session.keys():
        if request.method=='GET':
            all_users=User_details.objects.all()
            serializer= AllUserSerializers(all_users,many=True)
            return Response(serializer.data)


def logout(request):
    if 'blog_user' in request.session.keys():
        del request.session['blog_user']
        return redirect('login')
    else:
        return redirect('login')