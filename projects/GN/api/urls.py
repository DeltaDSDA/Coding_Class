from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/$', views.UserListView.as_view(), name='user'),
]
