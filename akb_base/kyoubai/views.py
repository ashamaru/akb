from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .models import Position

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'kyoubai/index.html'
    context_object_name = 'context'

    request_ref = None

    def get(self, request, *args, **kwargs):
        self.request_ref = request
        return super(IndexView, self).get(request, args, kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        if self.request_ref is not None:
            context['user'] = self.request_ref.user
        return context

    def get_queryset(self):
        return {
            "position_list": Position.objects.all()
        }


class FilteredIndexView(generic.ListView):
    template_name = 'kyoubai/index.html'
    context_object_name = 'context'

    def filter(self):
        # kwargs holds the values from the url, see urls.py for namespaces
        position_list = Position.objects.all()
        if (self.kwargs != None):
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

    #def get(self, request, *args, **kwargs):
     #   if request.user.is_authenticated:
      #      return HttpResponse('Account information should be displayed here')
       # return super(MyAccountView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/kyoubai/auctions')
        else:
            return HttpResponse('Login failed<br><a href="/kyoubai/myaccount">zurück</a>')


class ImpressumView(generic.ListView):
    template_name = 'kyoubai/impressum.html'
    context_object_name = 'passed_args'

    def get_queryset(self):
        return self.args

class SignUpView(generic.TemplateView):
    template_name = 'kyoubai/sign_up.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        new_user = User.objects.create_user(username, username + '@kyoubai.com', password)
        if new_user is not None:
            return HttpResponse('Account erfolgreich erstellt<br><a href="/kyoubai/auctions">zurück</a>')
        else:
            return HttpResponse('Account creation failed')

class LogoutView(generic.View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponse('Logout success<br><a href="/kyoubai/auctions">zurück</a>')
        else:
            return HttpResponse('You must be logged in to logout...<br><a href="/kyoubai/auctions">zurück</a>')
