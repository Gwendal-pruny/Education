from django import forms
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.db import connection
from django.db.utils import IntegrityError

class ContactForm(forms.Form):
    name = forms.CharField(label="Nom")
    email = forms.EmailField(label="Adresse e-mail")
    consent = forms.BooleanField(label="J'accepte le partage de ces données avec les partenaires officiels de la Rugby Tropical Cup", required=False)

class NewsletterView(FormView):
    template_name = "newsletter.html"
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.db_count_subscribers()
        return context

    # Cette fonction est appelée lorsque le formulaire est invalide
    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        # On se sert du contexte pour faire passer un message d'erreur
        context["alert"] = "Le formulaire est incomplet ou incorrect."
        # On utilise la fonction "shortcut" render_to_response pour renvoyer à nouveau cette page
        return self.render_to_response(context)

    # Cette fonction est appelée lorsque le formulaire est valide
    def form_valid(self, form):
        # Récupération des valeurs de chaque champ du formulaire
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        consent = form.cleaned_data["consent"]

        try:
            # On essaye d'ajouter les informations dans la BDD
            self.db_add_subscriber(email, name, consent)
        except IntegrityError:
            # En cas d'email déjà inscrit dans la base de données (= doublon),
            # on attrape l'erreur IntegrityError qui en découle afin
            # d'afficher à nouveau le formulaire, avec un message d'erreur.
            context = self.get_context_data()
            context["alert"] = "Cette adresse e-mail est déjà inscrite à la newsletter."
            return self.render_to_response(context)

        # On ajoute un message temporaire dans notre session
        self.request.session["homemessage"] = "Merci pour votre inscription à la newsletter."

        # On laisse la méthode d'origine renvoyer une réponse HTTP
        return super().form_valid(form)

    # Renvoie le compte des inscrits à la newsletter
    def db_count_subscribers(self):
        sqlquery = """
        SELECT COUNT(email)
        FROM newsletter;
        """

        # Une requête COUNT ne renvoie toujours qu'une ligne de résultats,
        # donc on utilise .fetchone()
        with connection.cursor() as cursor:
            cursor.execute(sqlquery)
            row = cursor.fetchone()

        # On nous renvoie toujours une liste de champs, mais on sait que l'on n'en a qu'un seul.
        # Autant le sélectionner directement ici afin d'avoir ce qui nous intéresse (le résultat du COUNT)
        count = row[0]
        return count

    # Ajoute un nouvel inscrit dans la base de données
    def db_add_subscriber(self, email, name, consent):
        sqlquery = """
        INSERT INTO newsletter VALUES (%s, %s, %s);
        """

        with connection.cursor() as cursor:
            cursor.execute(sqlquery, [email, name, consent])
