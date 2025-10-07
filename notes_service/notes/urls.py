from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('notes/create/', views.NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note_edit'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
]
