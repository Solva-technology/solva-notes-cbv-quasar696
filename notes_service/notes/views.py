from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Note
from .forms import NoteForm


class NoteMixin:
    model = Note


class NoteFormMixin:
    form_class = NoteForm


class NoteSuccessListMixin:
    success_url = reverse_lazy("notes:note_list")


class NoteEditPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        note = self.get_object()
        return self.request.user == note.author or self.request.user.is_staff


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    ordering = ["-created_at"]
    paginate_by = 10

    def get_queryset(self):
        return (
            Note.objects.select_related("author", "status")
            .prefetch_related("categories")
            .order_by("-created_at")
        )


class NoteDetailView(NoteMixin, DetailView):
    context_object_name = "note"


class UserDetailView(DetailView):
    model = User
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = self.object.note_set.select_related("status").all()
        return context


class NoteCreateView(LoginRequiredMixin, NoteMixin, NoteFormMixin, NoteSuccessListMixin, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создать заметку"
        return context


class NoteUpdateView(LoginRequiredMixin, NoteEditPermissionMixin, NoteMixin, NoteFormMixin, UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать заметку"
        return context


class NoteDeleteView(LoginRequiredMixin, NoteEditPermissionMixin, NoteMixin, NoteSuccessListMixin, DeleteView):
    pass
