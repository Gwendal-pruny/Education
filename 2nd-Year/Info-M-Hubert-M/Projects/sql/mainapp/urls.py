from django.urls import path
# Import des vues qui sont déclarées dans leur propre module (dossier)
from .views import HomeView, StadiumsView, NewsletterView, UpdateView

urlpatterns = (
    path("", HomeView.as_view(), name="home"),
    path("stadiums", StadiumsView.as_view(), name="stadiums"),
    path("newsletter", NewsletterView.as_view(), name="newsletter"),
    path("update", UpdateView.as_view(), name="update"),
)
