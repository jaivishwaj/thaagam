from django.urls import path
from dashboard import views


urlpatterns = [
    path("dashboard_login/", views.dashboard_login, name="dashboard_login"),
    path('list_users/', views.list_users, name='list_users'),
    path("dash_reg/", views.dash_reg, name="dash_reg"),
    path('user_control_panel/', views.user_control_panel, name='user_control_panel'),
]
