from django.shortcuts import render
from django.views import generic

from .models import Position

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'kyoubai/index.html'
    context_object_name = 'context'

    def filter(self):
        # kwargs holds the values from the url, see urls.py for namespaces
        position_list = Position.objects.all()

        if (self.kwargs['state'] == "used"):
            position_list = position_list.filter(state='used')
        elif (self.kwargs['state'] == "new"):
            position_list = position_list.filter(state='new')

        return position_list

    def get_queryset(self):
        return {
            "position_list": self.filter(),
        }


class MyAccountView(generic.TemplateView):
    template_name = 'kyoubai/myaccount.html'


class ImpressumView(generic.ListView):
    template_name = 'kyoubai/impressum.html'
    context_object_name = 'passed_args'

    def get_queryset(self):
        return self.args





