from django import views
from django.urls import path
from . import views


urlpatterns=[ 
    path('',views.home,name='home'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('update/<int:todo_id>/', views.update, name='update'),
]