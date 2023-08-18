from django.urls import path
from .views import HomeView, SignOutView,CustomLoginView, SignUpView

app_name='djangocrud'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="sign"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", SignOutView.as_view(), name="logout"),
    
]
