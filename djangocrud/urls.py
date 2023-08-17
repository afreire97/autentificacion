from django.urls import path
from .views import HomeView, SignUpView

app_name='djangocrud'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="sign"),
    
]
