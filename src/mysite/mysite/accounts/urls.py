from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('password/change/', views.CustomPasswordChangeView.as_view(), name='account_password_change'),
    path('profile/', views.ProfileView.as_view(), name='account_profile')
]