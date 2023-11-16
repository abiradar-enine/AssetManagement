from .views.asset_views import CreateAsset, UpdateAsset
from django.urls import path


urlpatterns = [
    path("new_asset", CreateAsset.as_view(), name="add_new_asset"),
    path("update_asset/<int:pk>", UpdateAsset.as_view(), name="update_asset"),
]
