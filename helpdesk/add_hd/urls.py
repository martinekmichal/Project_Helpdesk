from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path("user_detail/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("user_list/", UserListView.as_view(), name="user_list"),
    path("user_create/", UserCreateView.as_view(), name="user_create"),
    path("user_detail/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
    path("kontakt_detail/<int:pk>/edit/", UserUpdateView.as_view(), name="kontakt_edit"),
    path('HD_create/', views.helpdesk_create, name='HD_create'),
    path('HDD_list/', views.helpdesk_list, name='HDD_list'),


]