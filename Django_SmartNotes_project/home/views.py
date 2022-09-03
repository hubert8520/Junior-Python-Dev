from django.shortcuts import render
from datetime import date
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "home/signup.html"
    success_url = "/smart/notes"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("notes.list")

        return super().get(request, *args, **kwargs)


class NotesLogoutView(LogoutView):
    template_name = "home/logout.html"


class NotesLoginView(LoginView):
    template_name = "home/login.html"
    next_page = "/smart/notes"


class HomeView(TemplateView):
    template_name = "home/home.html"
    extra_context = {"today": date.today()}


"""
def home(request):
    return render(request, 'home/home.html', {'today':date.today()})
"""

"""
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"



@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
"""
