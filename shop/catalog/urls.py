from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
                  path('', views.index, name='index'),
                  path('index', views.index, name='index'),
                  path('about', views.about, name='about'),
                  path('thinners', views.thinners, name='thinners'),
                  path('ukr_thinners', views.ukrthinners, name='ukr_thinners'),
                  path('news', views.news, name='news'),
                  path('thinner/<int:thinner_pk>/', get_thinner),
                  path('ukrthinner/<int:ukrthinner_pk>/', get_ukrthinner),
                  path('new/<int:new_pk>/', get_news),
                  path('order', order),
                  path('contacts', views.contacts, name='contacts')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
