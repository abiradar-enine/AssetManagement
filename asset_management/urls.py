from django.urls import path
from .views.asset_views import AllAssets, CreateAsset, UpdateAsset, AllocateAsset
from .views.assetgroup_views import (
    AssetGroupCreateView,
    AssetGroupUpdateView,
    AssetGroupDeleteView,
    AssetGroupReportView,
    AssetGroupListView,
)


urlpatterns = [
    path("asset/list", AllAssets.as_view(), name="assets"),
    path("asset/new", CreateAsset.as_view(), name="add_new_asset"),
    path("asset/<int:pk>/edit", UpdateAsset.as_view(), name="update_asset"),
    path("asset/<int:pk>/allocate", AllocateAsset.as_view(), name="allocate_asset"),
]


urlpatterns += [
    path("assetgroup/new/", AssetGroupCreateView.as_view(), name="AssetGroup-create"),
    path(
        "assetgroup/<int:pk>/edit/",
        AssetGroupUpdateView.as_view(),
        name="AssetGroup-update",
    ),
    path(
        "assetgroup/<int:pk>/delete/",
        AssetGroupDeleteView.as_view(),
        name="AssetGroup-delete",
    ),
    path("assetgroup/list/", AssetGroupListView.as_view(), name="AssetGroup-list"),
    path(
        "assetgroup/report/", AssetGroupReportView.as_view(), name="AssetGroup-report"
    ),
    path("", AssetGroupReportView.as_view(), name="Welcome"),
]
