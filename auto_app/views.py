from django.shortcuts import render
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from .serializers import *
from .models import *
from rest_framework import generics, viewsets

#отображение всех автомобилей
class AutoList(generics.ListAPIView):
    queryset = AutoTechCHar.objects.all()
    serializer_class = AutoListSerializer

#отображение авто по вину
class AutoDetailList(generics.RetrieveAPIView):
    queryset = AutoTechCHar.objects.all()
    serializer_class = AutoListSerializer

#создание авто всех характеристик
class CreateAuto(generics.CreateAPIView):
    queryset = AutoTechCHar.objects.all()
    serializer_class = AutoCreateSerializer

#создание марки
class CreateAutoBrand(generics.CreateAPIView):
    queryset = AutoBrand.objects.all()
    serializer_class = CreateAutoBrand

#создание модели
class CreateAutoModel(generics.CreateAPIView):
    queryset = AutoModel.objects.all()
    serializer_class = CreateAutoModel


#-----------------------------------------------------









