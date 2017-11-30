from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, AnonymousUser

from .forms import LoginForm, BidForm

from .models import Article, Bid, Customer
from django.db.models import Max


class IndexView(generic.ListView):
    model = Article
    template_name = 'kyoubai/index.html'
    context_object_name = 'context'
    paginate_by = 5     # 1 just for testing
    queryset = Article.objects.all()

    request_ref = None

    def get(self, request, *args, **kwargs):
        self.request_ref = request
        return super(IndexView, self).get(request, args, kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        if self.request_ref is not None:
            context['user'] = self.request_ref.user
        return context


class FilteredIndexView(generic.ListView):
    template_name = 'kyoubai/index.html'
    context_object_name = 'context'
    paginate_by = 5     # 1 just for testing

    def filter(self):
        # kwargs holds the values from the url, see urls.py for namespaces
        position_list = Article.objects.all()
        if (self.kwargs != None):
            if (self.kwargs['state'] == "used"):
                position_list = position_list.filter(state='used')
            elif (self.kwargs['state'] == "new"):
                position_list = position_list.filter(state='new')
        return position_list

    def get_queryset(self):
        return self.filter()

from .delegate import Delegate

class PositionDetailView(generic.TemplateView):
    template_name = 'kyoubai/pos_detail.html'
    requested_pos = None
    bid_form = None

    def get(self, request, *args, **kwargs):
        self.bid_form = BidForm()
        if kwargs:
            self.requested_pos = kwargs['posid']
        if self.requested_pos is None:
            return Http404()
        return super(PositionDetailView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.bid_form = BidForm(request.POST)
        if kwargs:
            self.requested_pos = kwargs['posid']
        if self.bid_form.is_valid():
            delegate = Delegate()
            bid = Bid()
            bid.b_amount = self.bid_form.cleaned_data['amount']
            bid.b_customer = Customer.objects.get(c_user__exact=request.user)
            print(str(self.requested_pos))
            bid.b_article = Article.objects.get(pk=self.requested_pos)
            delegate.processBid(bid)
            res = delegate.res
            print(res)
            if res is 'Valid':
                return HttpResponse('Success!')
            else:
                return HttpResponse('Failed !')
        else:
            return super(PositionDetailView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PositionDetailView, self).get_context_data()
        context['cur_pos'] = self.requested_pos
        context['article'] = Article.objects.get(a_id=self.requested_pos)
        context['bid_form'] = self.bid_form
        mbid = Bid.objects.all().filter(b_article__a_id = self.requested_pos).aggregate(Max('b_amount'))
        context['mbid'] = mbid['b_amount__max'];
        return context


class MyAccountView(generic.TemplateView):
    template_name = 'kyoubai/myaccount.html'
    login_form = None
    user = None

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        self.login_form = form
        self.user = request.user
        # if request.user.is_authenticated:
        #    return HttpResponse('Account information should be displayed here')
        return super(MyAccountView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        self.login_form = form
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['user_name'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/kyoubai/auctions')
            else:
                return HttpResponse('Login failed<br><a href="/kyoubai/myaccount">zurück</a>')
        else:
            return super(MyAccountView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MyAccountView, self).get_context_data()
        context['login_form'] = self.login_form
        print(self.user)
        if self.user is not None and self.user.id is not None:
            customer = Customer.objects.get(c_user = self.user)
            print(customer)
            context['customer'] = customer
        return context


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
