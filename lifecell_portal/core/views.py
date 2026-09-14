from django.utils import timezone
from django.views.generic import TemplateView

from portal.models import (
    News,
    Event,
    Announcement,
    Material,
)


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["news"] = News.objects.all()[:3]

        context["events"] = Event.objects.filter(
            date__gte=timezone.now()
        )[:3]

        context["announcements"] = Announcement.objects.all()[:3]

        context["materials"] = Material.objects.all()[:3]

        return context