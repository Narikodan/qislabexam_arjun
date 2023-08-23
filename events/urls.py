from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_section/', views.admin_section, name='admin_section'),
    path('add_event/', views.add_event, name='add_event'),
]
