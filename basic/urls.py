
from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.index , name='index'),
   path('login' , views.loginPage , name='loginPage'),
   path('register' , views.register , name='register'),
   path('profile' , views.profile , name='profile'),
   path( 'logout' , views.logoutPage , name='logoutPage'),
   path('newPost' , views.newPost , name='newPost'),

   path('like/<int:id>' , views.like , name='like'),
    path('detailed_post/<int:pk>/' , views.detailedPost , name='detailedPost'),

    path('newComment/<int:pk>/' , views.newComment , name='newComment')
]