from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='url_index_login'),
    path('login/', views.login, name='url_login'),
    path('logout/', views.logout, name='url_logout'),
    path('cadastro/', views.cadastro, name='url_cadastro'),
    path('dashboard/', views.dashboard, name='url_dashboard'),
]