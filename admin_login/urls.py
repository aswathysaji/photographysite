from admin_login import views
from django.urls import path

urlpatterns = [
    path('login',views.login_admin,name='login'),
    path('logout',views.logout_admin,name='logout')
]