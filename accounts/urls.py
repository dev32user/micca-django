from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('change-password/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/pw_change.html'),
         name='pw_change')
]
