from django.urls import path
# On importe les vues qui sont déclarées dans leur propre dossier (module)
from .views import HomeView, AboutView

urlpatterns = (
    path("", HomeView.as_view(), name="home"),
    path("a-propos", AboutView.as_view(), name="about"),
)
