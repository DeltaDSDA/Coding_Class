from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.board_view),
    path('support_board/', views.support_board_view),
]
