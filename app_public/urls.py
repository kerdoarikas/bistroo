from django.urls import path
from . import views

urlpatterns = [
    path('', views.PublicHomeView.as_view(), name='public_home'),
    # Add more URLs for other views if needed
]
