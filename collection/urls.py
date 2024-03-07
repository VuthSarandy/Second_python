from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from  . import views as collection_view
from . import views
from .views import *

app_name = 'collection'
urlpatterns = [
    re_path('^person/$', collection_view.home_page, name='person'),   
    re_path('^person/(?P<id>\d+)/$', collection_view.find_person, name='find_person'),

    re_path('^api_person/$', collection_view.api_person, name='api_person'),

    # re_path('^person/(?P<id>\d+)/(?P<name>\D+)$', collection_view.find_person_id_name, name='find_person'),
]

