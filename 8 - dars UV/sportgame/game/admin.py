from django.contrib import admin
from .models import SportType, Category, Rule, Equipment

# Register your models here.

admin.site.register(SportType)
admin.site.register(Category)
admin.site.register(Rule)
admin.site.register(Equipment)
