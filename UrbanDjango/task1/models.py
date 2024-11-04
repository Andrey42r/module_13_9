from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, default=0, decimal_places=2, null=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=10, default=0, decimal_places=2, null=True)
    size = models.DecimalField(max_digits=10, default=0, decimal_places=2, null=True)
    description = models.CharField(default='Game', max_length=100000000)
    age_limited = models.BooleanField(False)
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title

