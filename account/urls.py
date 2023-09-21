from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('staffdashboard/', views.staffdashboard, name='staffdashboard'),
    path('delete_button/<str:id>/', views.delete_button, name='delete_button'),
    path('update_listing_form', views.updateListingForm, name='update_listing_form'),
    path('update_listing/<str:id>/', views.update_listing, name='update_listing'),
]
