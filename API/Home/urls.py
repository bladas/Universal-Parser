from rest_framework import routers
from django.urls import path, include

from API.Home import views

# router = routers.DefaultRouter()
# router.register(r'', views.HomeView)

urlpatterns = [
    path('',views.HomeView.as_view())
]