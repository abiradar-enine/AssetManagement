from .views.asset_views import CreateAsset
from .views.assetgroup_views import *
from django.urls import path


urlpatterns = [
    path("new_asset", CreateAsset.as_view(), name="add_new_asset"),
    # path("update_asset/<int:pk>", UpdateAsset.as_view(), name="update_asset"),
]


urlpatterns = [
    path('AssetGroup/new/', AssetGroupCreateView.as_view(), name='AssetGroup-create'),
    path('AssetGroup/<int:pk>/edit/', AssetGroupUpdateView.as_view(), name='AssetGroup-update'),
    path('AssetGroup/<int:pk>/delete/', AssetGroupDeleteView.as_view(), name='AssetGroup-delete'),
    path ('AssetGroup/list/', AssetGroupListView.as_view(), name='AssetGroup-list')
]