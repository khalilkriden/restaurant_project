from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('edit_dish/<int:pk>/', views.edit_dish, name='edit_dish'),
    path('delete_dish/<int:pk>/', views.delete_dish, name='delete_dish'),
    path('reserve/', views.reserve, name='reserve'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
