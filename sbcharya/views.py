from django.views.generic import TemplateView
from timeline.models import Timeline
from work.models import Work
from websetting.models import Websetting


class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["timelines"] = Timeline.objects.all()
        data["works"] = Work.objects.all()
        data["websetting"] = Websetting.objects.get(id=1)
        return data