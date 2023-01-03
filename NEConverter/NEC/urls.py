from django.urls import path
from . import views

urlpatterns = [
    path('dc', views.neview),
    path('', views.con),
    path('crop/<str:pk>/', views.conId)
]
