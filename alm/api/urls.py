from django.urls import path, include
from .views import AccountList
app_name = "api"
urlpatterns = [
        path("", AccountList.as_view(), name="list"),
]