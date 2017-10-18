from django.conf.urls import url
from .views import LugaresApi,LugaresHasPersonas

urlpatterns = [
    url(r'/hasPersonas', LugaresHasPersonas.as_view()),
    url(r'^$', LugaresApi.as_view())
]