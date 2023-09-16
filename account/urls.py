from django.urls import path
from . import views
from .views import AppointmentList, AppointmentView

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete_button/<str:id>/', views.delete_button, name='delete_button'),
    path('appointment', AppointmentList.as_view(), name='appointment'),
    path('appointment_view', AppointmentView.as_view(), name='appointment_view'),
]
