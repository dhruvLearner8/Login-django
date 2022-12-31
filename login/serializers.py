from rest_framework import serializers
from .models import User_details
class AllUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User_details 
        fields = ['email','full_name','age','dob']
