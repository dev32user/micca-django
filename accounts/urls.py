from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='accounts/pw_change.html'),
         name='pw_change'),
    path('profile/', views.get_member, name='get_member'),
    path('profile/<int:member_id>/', views.get_member, name='get_member_id'),
    path('change-profile/', views.update_member, name='profile_change'),
]
