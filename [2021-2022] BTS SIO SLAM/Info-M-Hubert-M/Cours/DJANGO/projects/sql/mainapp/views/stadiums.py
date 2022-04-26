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
        Voici ce à quoi devrait ressembler le contenu de cette clé :
        [
            [1, "Eden Park", "Auckland", -36.875488, 174.744684],
            [2, "Sky Stadium", "Wellington", -41.273002, 174.785872],
            [3, "Mt Smart Stadium", "Auckland", -36.918429, 174.812345],
            [4, "FMG Stadium Waikato", "Hamilton", -37.781670, 175.269632]
        ]
        """
        return context
    
    def read_stadiums(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, location, latitude, longitude FROM stadium")
            rows = cursor.fetchall()
        return rows

