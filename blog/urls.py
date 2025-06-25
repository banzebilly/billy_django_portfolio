
from django.urls import path, include

from . import views

urlpatterns = [
 
    path('blog_home/', views.blog_home, name='blog_home'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),  # Detail view
   
   

]
