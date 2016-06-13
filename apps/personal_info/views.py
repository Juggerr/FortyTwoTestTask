from django.views.generic import TemplateView

from .models import PersonalInfo


class PersonalInfoDetail(TemplateView):

    template_name = "personal_info/pages/main.html"

    def get_context_data(self, **kwargs):
        context = super(PersonalInfoDetail, self).get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.last()
        return context
