from django.urls import path
from . import views

urlpatterns = [
    path('', views.article),
    path('new/', views.new),
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
]
