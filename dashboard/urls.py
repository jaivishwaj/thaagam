from django.contrib import admin
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_control_panel/', views.user_control_panel, name='user_control_panel'),
    path('superuser_dashboard/', views.superuser_dashboard, name='superuser_dashboard'),
    path('staff_dashboard/<int:staff_id>/', views.staff_dashboard, name='staff_dashboard'),
    path("dash_reg/", views.register, name="dash_reg"),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),


]

