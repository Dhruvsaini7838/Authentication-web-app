from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),

]