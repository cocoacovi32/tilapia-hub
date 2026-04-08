from django.db import models

class Fish(models.Model):
    name = models.CharField(max_length=100)
    price_per_kg = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.total}"