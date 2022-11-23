from django.urls import path

from . import views

urlpatterns = [
    path('persons/', views.person_list, name='person_list'),
    path('persons/<int:pk>/', views.person_detail, name='person_detail'),
    path('persons/update/<int:pk>/', views.person_update_delete, name='person_update_delete'),
    path('persons/delete/<int:pk>/', views.person_update_delete, name='person_update_delete'),
    path('', views.index, name='index'),
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail)
]