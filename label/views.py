from django.conf import settings
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = f"label/labelprint.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            edc_packages=["not available"],
            third_party_packages=["not available"],
            installed_apps=settings.INSTALLED_APPS,
        )
        return context
