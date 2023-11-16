from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from ..models import Asset


class CreateAsset(CreateView):
    template_name = "addAsset.html"
    model = Asset
    fields = [
        "name",
        "description",
        "asset_code",
        "asset_group",
        "asset_model_number",
        "asset_serial_number",
    ]


class UpdateAsset(UpdateView):
    template_name = "updateAsset.html"
    model = Asset
    fields = [
        "name",
        "description",
        "asset_code",
        "asset_group",
        "asset_model_number",
        "asset_serial_number",
    ]


class AllAssets(ListView):
    template_name = "assets.html"
    context_object_name = "assets"

    def get_queryset(self):
        return Asset.objects.all()
