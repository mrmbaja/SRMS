from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_results/', views.add_results, name='add_results'),
    path('view_results/', views.view_results, name='view_results'),
    path('results/<int:id>/', views.result_details, name='result_details'),
]

