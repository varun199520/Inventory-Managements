from django.urls import path
from . import views

app_name = 'student_management'

urlpatterns = [
    path('create/', views.student_create, name='student_create'),
    path('list/', views.student_list, name='student_list'),
    path('<uuid:pk>/', views.student_profile, name='student_profile'),
    path('<uuid:pk>/edit/', views.student_edit, name='student_edit'),
    path('<uuid:pk>/delete/', views.student_delete, name='student_delete'),
]
