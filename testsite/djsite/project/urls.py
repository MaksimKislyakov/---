from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/create_google_document/', views.create_google_document, name='create_google_document'),
    path('project/<int:project_id>/create_google_slide/', views.create_google_slide, name='create_google_slide'),
]