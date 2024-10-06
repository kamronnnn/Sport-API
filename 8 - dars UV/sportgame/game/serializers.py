from rest_framework.serializers import ModelSerializer
from .models import SportType, Category, Rule, Equipment



class SportTypeSerializer(ModelSerializer):
    class Meta:
        model = SportType
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RuleSerializer(ModelSerializer):
    class Meta:
        model =Rule
        fields = '__all__'


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model =Equipment
        fields = '__all__'
