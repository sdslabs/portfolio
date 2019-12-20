from django.conf.urls import url

from .import views


urlpatterns = [
    url(r'^$', views.get_events, name='get_events'),
    url(r'updates', views.get_event_updates, name='get_news_updates')
]
