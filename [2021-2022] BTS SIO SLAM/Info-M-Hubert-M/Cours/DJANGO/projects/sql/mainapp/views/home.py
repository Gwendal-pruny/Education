from django.views.generic import TemplateView
from django.db import connection

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["organisateur"] = "World Rugby"
        context["event"] = self.read_event()

        # On rajoute un message dans notre contexte s'il y en a un dans la session
        # (cf projet Minimal 5)
        if "homemessage" in self.request.session:
            context["message"] = self.request.session["homemessage"]
            del self.request.session["homemessage"]

        return context

    # Récupère les informations liées à l'événement numéro 1
    def read_event(self):
        sqlquery = """
        SELECT event.start, stadium.name, home.country, away.country
        FROM event
        INNER JOIN stadium ON event.stadium_id = stadium.id
        INNER JOIN team AS home ON event.team_home_id = home.id
        INNER JOIN team AS away ON event.team_away_id = away.id
        WHERE event.id = %s;
        """

        with connection.cursor() as cursor:
            # Le 2nd argument sert à injecter des valeurs au sein d'une requête
            cursor.execute(sqlquery, [1])
            row = cursor.fetchone()
        return row
