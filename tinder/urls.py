from django.urls import path 
from .import views

urlpatterns = [
    path('',views.home),
    path('api/',views.ApisView.as_view()),
    path('add/', views.AddView.as_view()),
    path('delete<int:pk>/', views.DeleteView.as_view()),
]
