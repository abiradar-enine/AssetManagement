# views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from ..models import AssetGroup
from django.views import View
from django.shortcuts import render

class AssetGroupCreateView(CreateView):
    model = AssetGroup
    template_name = "AssetGroup_form.html"
    fields = "__all__"
    success_url = reverse_lazy("AssetGroup-list")


class AssetGroupUpdateView(UpdateView):
    model = AssetGroup
    template_name = "AssetGroup_form.html"
    fields = "__all__"
    success_url = reverse_lazy("AssetGroup-list")


class AssetGroupDeleteView(DeleteView):
    model = AssetGroup
    template_name = "AssetGroup_confirm_delete.html"
    success_url = reverse_lazy("AssetGroup-list")  # Redirect after deletion


class AssetGroupListView(ListView):
    model = AssetGroup
    template_name = "AssetGroup_list.html"
    context_object_name = "AssetGroup_list"
    ordering = ["-id"]


class AssetGroupReportView(View):
    template_name = 'AssetGroup_report.html'

    def get(self, request, *args, **kwargs):
        asset_groups = AssetGroup.objects.prefetch_related('assets__assetallocation_set').all()

        context = {'asset_groups': asset_groups}
        return render(request, self.template_name, context)