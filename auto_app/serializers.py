from rest_framework import serializers
from .models import *

#оттображене всех автомобилей
class AutoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoTechCHar
        fields = '__all__'


#отображение автомобилей по VIN
class AutroDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoTechCHar
        fields = ['vin']

#создание автомобилей
class AutoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoTechCHar
        fields = ['brand, model']

#создание марок
class CreateAutoBrand(serializers.ModelSerializer):
    class Meta:
        model = AutoBrand
        fields = ['name']

#создание моделей
class CreateAutoModel(serializers.ModelSerializer):
    class Meta:
        model = AutoModel
        fields = ['name_model']

#-----------------------------------------------------

