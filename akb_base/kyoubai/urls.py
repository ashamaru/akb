from django.conf.urls import url
from . import views

app_name = 'kyoubai'
urlpatterns = [
    # /kyoubai/auctions
    url(r'^auctions/$', views.IndexView.as_view(), name='index'),
    # /kyoubai/auctions/<values>
    url(r'^auctions/(?P<state>[\w]+)-?(?P<price_min>[\w]+)?-?(?P<price_max>[\w]+)?$',
        views.FilteredIndexView.as_view(), name='filter_index'),
    # /kyoubai/auctions/pos/<id>
    url(r'^auctions/pos/(?P<posid>[0-9]+)$', views.PositionDetailView.as_view(), name='pos'),
    # /kyoubai/impressum
    url(r'^impressum$', views.ImpressumView.as_view(), name='impressum'),
    # /kyoubai/myaccount
    url(r'^myaccount$', views.MyAccountView.as_view(), name='myaccount'),
    # /kyoubai/sign_up
    url(r'^sign_up$', views.SignUpView.as_view(), name='sign_up'),
    # /kyoubai/logout
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
]
