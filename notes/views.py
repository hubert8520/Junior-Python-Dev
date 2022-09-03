from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NotesForm
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes/"
    template_name = "notes/notes_delete.html"


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes/"
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    success_url = "/smart/notes/"
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


"""
def list_of_notes(request):
    notesList = Notes.objects.all()
    return render(request, "notes/notes_list.html", {"notes": notesList})
"""


class NotesDetailView(DetailView):  # class-based view
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_details.html"


"""
def get_details(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Something's wrong. The note doesn't exist")
    return render(request, "notes/note_details.html", {"note": note})
"""
