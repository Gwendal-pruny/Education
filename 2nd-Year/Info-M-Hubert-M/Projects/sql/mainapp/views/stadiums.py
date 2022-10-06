from django.views.generic import TemplateView
from django.db import connection

class StadiumsView(TemplateView):
    template_name = "stadiums.html"

    def get_context_data(self, **kwargs):
        # On récupère toujours le contexte tel qu'il est préparé par Django,
        # d'où l'appel à la fonction originale .get_context_data() via le super()
        context = super().get_context_data(**kwargs)

        # On rajoute une clé au contexte, dont le contenu sera renvoyé par notre fonction
        context["stadiums"] = self.read_stadiums()
        """
        Voici ce à quoi devrait ressembler le contenu associé à cette clé :
        [
            [1, 'Ajinomoto Stadium', 'Tokyo', 35.664051, 139.527175],
            [2, 'Toyota Stadium', 'Tokyo', 35.084470, 137.170923],
            [3, 'Noevir Stadium Kobe', 'Kobe', 34.656683, 135.168941],
            [4, 'Best Denki Stadium', 'Fukuoka', 33.585855, 130.460784]
        ]
        """
        return context
    
    def read_stadiums(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, location, latitude, longitude FROM stadium")
            rows = cursor.fetchall()
        return rows

