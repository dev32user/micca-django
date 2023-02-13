from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.article, name='home'),
    path('new/', views.new, name='new_article'),
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
]
