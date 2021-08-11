from django.urls import path, include
from .views import AccountList
app_name = "blog"
urlpatterns = [
        path("", AccountList.as_view(), name="list"),
]
