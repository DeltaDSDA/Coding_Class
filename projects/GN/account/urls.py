from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('user/', views.user_list_view),
]
