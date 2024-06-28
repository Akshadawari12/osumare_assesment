from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.first, name="first"),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('update/<str:id>', views.update, name='update'),
    
]