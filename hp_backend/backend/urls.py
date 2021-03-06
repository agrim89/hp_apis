from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^user/', views.UserDetail.as_view()),
    url(r'^company/', views.CompanyDetail.as_view()),
    url(r'^retrieve/', views.ListDetail.as_view()),
    url(r'^retrieve_view/', views.NewListDetail.as_view()),
    url(r'^validate/', views.LoginVerify.as_view()),
    url(r'^forgot_password/', views.ForgotPassword.as_view()),
    url(r'^change_password/', views.ChangePassword.as_view()),
    url(r"^report/", views.report_api),
    url(r"^send_email/", views.send_email),

]
