from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        user = User.objects.all()
        model = User
        fields = '__all__' 