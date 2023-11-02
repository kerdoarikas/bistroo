from django.views.generic import TemplateView

class PublicHomeView(TemplateView):
    template_name = 'app_public/public_home.html'
