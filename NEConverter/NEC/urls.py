from django.urls import path
from . import views

urlpatterns = [
    path('', views.neview),
    path('img', views.con),
    path('crop/<str:pk>/', views.conId)
]