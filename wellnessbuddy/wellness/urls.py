from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_scores/', views.submit_scores, name='submit_scores'),
    path('generate_plan/<phone_number>/', views.generate_plan, name='generate_plan'),
]
