from .forms import RegisterUserForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class UserCreateView(CreateView):
    form_class = RegisterUserForm
    model = get_user_model()
    success_url = '/login/'


class UserDetailView(DetailView, LoginRequiredMixin):
    model = get_user_model()
    login_url = '/login/'

    def get_object(self):
        """
        An authenticated user may only access the details of itself
        """
        return get_object_or_404(self.model, pk=self.request.user.pk)
