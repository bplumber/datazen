from django.urls import path
from . import views
from django.conf.urls import url 

urlpatterns = [path("", views.home, name="home"),
               path('register',views.register,name="register"),
               path('backend',views.backend,name="backend"),
               path('frontend',views.frontend,name="frontend"),
               path('datascience',views.datascience,name="datascience"),
               path('datasciencequiz',views.datasciencequiz,name="datasciencequiz"),
               path('frontendquiz',views.frontendquiz,name="frontendquiz"),
               path('backendquiz',views.backendquiz,name="backendquiz")




]