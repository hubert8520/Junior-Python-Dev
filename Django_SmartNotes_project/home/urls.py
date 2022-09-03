from django.urls import path
from .views import HomeView, NotesLoginView, NotesLogoutView,SignupView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path('login/', NotesLoginView.as_view(), name="login"),
    path('logout/', NotesLogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
]
