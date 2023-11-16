from django.db import models
from datetime import datetime
from django.utils import timezone


class AssetGroup(models.Model):
    name = models.CharField(max_length=128, blank=False, unique=True)
    description = models.CharField(max_length=255, default="", null=True, blank=True)

    class Meta:
        verbose_name = "Asset Group"
        verbose_name_plural = "Asset Groups"

    def __str__(self):
        return self.name


class Asset(models.Model):
    CHOICES = (
        ("OPERATIONAL", "Operational"),
        ("NONOPERATIONAL", "Nonoperational"),
        ("MISSING", "Missing"),
    )

    name = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=255, default="", null=True, blank=True)
    asset_code = models.CharField(max_length=128, blank=False, unique=True)
    asset_group = models.ForeignKey(
        AssetGroup, related_name="assets", on_delete=models.CASCADE
    )
    asset_model_number = models.CharField(max_length=128, null=False, blank=False)
    asset_serial_number = models.CharField(
        max_length=128, default="", blank=True, null=True
    )
    asset_purchase_date = models.DateTimeField(default=timezone.now)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=CHOICES, default="OPERATIONAL", max_length=128)

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"

    
    def __str__(self):
        return f'{self.name} - {self.asset_code}'


class AssetAllocation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255, default="Office")

    class Meta:
        verbose_name = "Asset Allocation"
        verbose_name_plural = "Asset Allocations"