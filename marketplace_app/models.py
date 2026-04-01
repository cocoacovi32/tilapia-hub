# marketplace_app/models.py
# marketplace_app/models.py

from django.db import models
from django.conf import settings   # ✅ correct import


# -----------------------------
# Farmer Model
# -----------------------------
class Farmer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,   # ✅ FIXED HERE
        on_delete=models.CASCADE,
        related_name="farmers",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# -----------------------------
# Fish Model (Marketplace Listings)
# -----------------------------
class Fish(models.Model):
    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name="fish",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)   # e.g. Tilapia
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.price}"


# -----------------------------
# Product Model (Optional)
# -----------------------------
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name