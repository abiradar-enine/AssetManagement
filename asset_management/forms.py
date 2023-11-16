from django import forms
from .models import AssetGroup, Asset, AssetAllocation


class CreateAsset(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ["name", "description", "asset_code", "asset_group", "asset_model_number", "asset_serial_number"]
 