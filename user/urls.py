from django.contrib.auth.views import LoginView
from django.urls import path
from .views import UserRegisterView, UserLogoutView

app_name = 'user'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html', next_page='core:index'), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]