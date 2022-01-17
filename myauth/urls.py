from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signin/', views.sign_in, name='signin'),
]