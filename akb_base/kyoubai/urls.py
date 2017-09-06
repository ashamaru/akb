from django.conf.urls import url
from . import views

app_name = 'kyoubai'
urlpatterns = [
    # /kyoubai/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /kyoubai/impressum
    url(r'^impressum$', views.ImpressumView.as_view(), name='impressum'),

]
