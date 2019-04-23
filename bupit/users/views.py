from .forms import RegisterUserForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


# Create your views here.
class UserCreateView(CreateView):
    form_class = RegisterUserForm
    model = get_user_model()
    success_url = reverse_lazy('admin:login')


class UserDetailView(DetailView):
    model = get_user_model()

    def get_object(self):
        """
        An authenticated user may only access the details of itself
        """
        return get_object_or_404(self.model, pk=self.request.session.user.pk)



