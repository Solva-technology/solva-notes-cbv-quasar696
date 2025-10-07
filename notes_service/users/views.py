from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("notes:note_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
