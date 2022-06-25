from django.shortcuts import render
from rest_framework import status, viewsets, mixins 
from rest_framework.response import Response 
from django.http import Http404

from rest_framework.views import APIView
from .models import User 
from .serializers import UserSerializer
# Create your views here. 

class UserViewSet(viewsets.GenericViewSet, 
                mixins.ListModelMixin, 
                APIView): 

    serializer_class = UserSerializer   # 이 클래스형 view 에서 사용할 시리얼라이저를 선언

    def get_queryset(self):
        return User.objects.all()

    def add(self, request): 
        musics = User.objects.filter(**request.data)
        if musics.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        music_serializer = UserSerializer(data=request.data, partial=True)
        if not music_serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        music = music_serializer.save()

        return Response(UserSerializer(music).data, status=status.HTTP_201_CREATED)
        

