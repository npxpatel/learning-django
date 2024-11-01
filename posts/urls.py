from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    # path('<id>/', views.post),  by default it will take the id as string
    path('<int:id>/', views.post, name = 'post'), 
]