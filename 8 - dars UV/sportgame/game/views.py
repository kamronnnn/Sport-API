from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from .models import SportType, Category, Rule, Equipment
from .serializers import SportTypeSerializer, CategorySerializer, RuleSerializer, EquipmentSerializer


# Create your views here.


class SportTypeViewSet(ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer
    authentication_classes = [TokenAuthentication]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]


class RuleViewSet(ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer


class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
