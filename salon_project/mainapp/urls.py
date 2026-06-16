from django.urls import path 
from mainapp import views
from django.contrib.auth import logout

urlpatterns = [
    path('' , views.home , name='home'),
    path('about' , views.about , name='about'),
    path('register' , views.register_view , name='register'),
    path('login' , views.login_view , name='login'),
    path('services' , views.services , name='services'),
    path('create_appointment/<int:service_id>/', views.create_appointment, name="create_appointment"),
    path('add_review/<int:service_id>/' , views.add_review , name="add_review" ),
    path('account' , views.my_account , name='account'),
    path('logout' , views.logout_view , name='logout'),
]
