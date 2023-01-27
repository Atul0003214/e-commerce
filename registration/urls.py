from django.urls import path,include
from . import views



urlpatterns = [
    path('login/', views.LoginClass.as_view(),name='login'),
    path('logout/', views.LogoutClass.as_view(),name='logout'),
    path('password_reset/', views.PasswordResetClass.as_view(),name='admin_password_reset'),
    path('signup/', views.SignUp,name='signup'),
    path(
        "password_reset/done/",
        views.PasswordRestDoneClass.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmViewClass.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteViewClass.as_view(),
        name="password_reset_complete",
    ),
       
]
