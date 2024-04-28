from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name=""),
    path("signin", views.signin, name="signin"), 
    path("login", views.loginFunction, name="login"),
    path("home", views.home, name="home"),
    path("logout", views.logoutFunc, name="Logout"),
    path("chat/<str:pk>", views.chatFunc,)
]