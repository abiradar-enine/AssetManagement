from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import AssetGroup, Asset, AssetAllocation
from .forms import CreateAsset


class CreateAsset(CreateView):
    template_name = 'addAsset.html'
    model = Asset
    success_url = ''
    form_class = CreateAsset