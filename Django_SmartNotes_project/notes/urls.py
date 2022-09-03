from django.urls import path
from .views import NotesCreateView, NotesListView, NotesDetailView, NotesUpdateView, NotesDeleteView

urlpatterns = [
    path('notes/', NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', NotesDetailView.as_view(), name='notes.details'),
    path('notes/<int:pk>/edit', NotesUpdateView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete', NotesDeleteView.as_view(), name='notes.delete'),
    path('notes/new', NotesCreateView.as_view(), name='notes.new'),
]