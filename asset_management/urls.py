from .views.asset_views import CreateAsset
from django.urls import path


urlpatterns = [
    path("new_asset", CreateAsset.as_view(), name="add_new_asset"),
]
