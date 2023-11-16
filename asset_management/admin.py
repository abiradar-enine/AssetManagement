from django.contrib import admin
from .models import AssetGroup, Asset, AssetAllocation
# Register your models here.

@admin.register(AssetGroup)
class AssetGroupAdmin(admin.ModelAdmin):
    model_fields = '__all__'

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    model_fields = '__all__'

@admin.register(AssetAllocation)
class AssetAllocationAdmin(admin.ModelAdmin):
    model_fields = '__all__'