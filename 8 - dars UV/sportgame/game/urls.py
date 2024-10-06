from django.urls import path, include
from rest_framework import routers
from .views import SportTypeViewSet, CategoryViewSet, RuleViewSet, EquipmentViewSet

router = routers.SimpleRouter()

router.register('sports-types', SportTypeViewSet)
router.register('categories', CategoryViewSet)
router.register('rules', RuleViewSet)
router.register('equipments', EquipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]