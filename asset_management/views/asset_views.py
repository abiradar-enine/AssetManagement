from math import ceil
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from ..models import Asset, AssetAllocation


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
        "status",
    ]


class AllAssets(ListView):
    template_name = "assets.html"
    context_object_name = "assets"
    paginate_by = 30

    def get_queryset(self):
        return Asset.objects.all()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        page_number = int(self.request.GET.get("page", 1))
        context["page_number"] = page_number
        records_per_page = self.paginate_by
        total_records = len(Asset.objects.all())
        context["last"] = ceil(total_records / records_per_page)
        remaining_records = total_records - ((page_number - 1) * records_per_page)
        context["has_more_records"] = remaining_records > records_per_page
        return context


class AllocateAsset(UpdateView):
    template_name = "asset_allocate.html"
    model = AssetAllocation
    fields = "__all__"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        asset = get_object_or_404(queryset, asset_id=self.kwargs["pk"])
        return asset
