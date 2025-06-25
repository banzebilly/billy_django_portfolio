
from django.urls import path, include

from . import views

urlpatterns = [
 
    path('work/', views.work, name='work'),

    path('<int:pk>/', views.work_detail, name='work_detail'),  # Detail view
   
   

]
