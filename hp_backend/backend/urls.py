from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^user/', views.UserDetail.as_view()),
    url(r'^company/', views.CompanyDetail.as_view()),
    url(r'^retrieve/', views.ListDetail.as_view()),
    url(r'^validate/', views.LoginVerify.as_view()),
    url(r'^forgot_password/', views.ForgotPassword.as_view()),
]
