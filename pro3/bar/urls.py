from django.urls import path
from . import views
from django.contrib.auth import views as views_auth

urlpatterns = [
    path('', views.signin, name="signin"),
    path('index', views.index, name="index"),
    path('signout', views.signout, name="signout"),
    path('signup', views.signup, name="signup"),
    path('change_password', views_auth.PasswordChangeView.as_view(template_name= "bar/change_password.html", success_url ='change_success'), name="change_password"),
    path('change_success', views.change_success, name="change_success"),
    path('password_reset', views_auth.PasswordResetView.as_view(template_name = "bar/password_reset.html"), 
         name="password_reset"),
    path('password_reset_done', views_auth.PasswordResetDoneView.as_view(template_name = "bar/password_reset_done.html"), 
         name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>', views_auth.PasswordResetConfirmView.as_view(template_name = "bar/password_reset_confirm.html"), 
         name="password_reset_confirm"),
    path('password_reset_complete', views_auth.PasswordResetCompleteView.as_view(template_name = "bar/password_reset_complete.html"), 
         name="password_reset_complete"),
     path('staff', views.staff, name="staff"),
     path('update_employee/<int:employee_id>', views.update_employee, name="update_employee"),
     path('delete_employee/<int:employee_id>', views.delete_employee, name="delete_employee"),
]