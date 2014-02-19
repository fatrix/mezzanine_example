from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r"^webservice/heartbeat/", 'heartbeat.views.heartbeat_service'),
)