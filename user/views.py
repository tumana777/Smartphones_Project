from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import UserRegisterForm


class UserRegisterView(CreateView):

    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('user:login')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('user:login')
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
