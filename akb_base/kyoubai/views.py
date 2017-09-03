from django.shortcuts import render
from django.views import generic

from .models import Position

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'kyoubai/index.html'
    context_object_name = 'position_list'

    def get_queryset(self):
        return Position.objects

