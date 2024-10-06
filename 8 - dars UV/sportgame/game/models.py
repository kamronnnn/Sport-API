from django.db import models

# Create your models here.


class SportType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Rule(models.Model):
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Equipment(models.Model):
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.name


