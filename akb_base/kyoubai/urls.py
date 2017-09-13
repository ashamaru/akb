from django.conf.urls import url
from . import views

app_name = 'kyoubai'
urlpatterns = [
    # /kyoubai/
    url(r'^(?P<state>[\w]+)?$', views.IndexView.as_view(), name='index'),
    # /kyoubai/impressum
    url(r'^impressum$', views.ImpressumView.as_view(), name='impressum'),
    # /kyoubai/myaccount
    url(r'^myaccount$', views.MyAccountView.as_view(), name='myaccount'),

]
