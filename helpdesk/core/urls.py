from django.urls import path
from .views import *
from django.contrib.auth import views as helpdesk


urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("HD_list/", hd_list_page, name="HD_list"),
    path("profile/", profile_page, name="profile"),
    path('register/', register_page, name='register'),
    path('login/', helpdesk.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', helpdesk.LogoutView.as_view(template_name='logout.html'), name='logout'),
]