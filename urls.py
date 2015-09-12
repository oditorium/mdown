from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.example, name='index'),
    url(r'^example$', views.example, name='example'),
    url(r'^wholepgmd$', views.whole_page_is_markdown, name='whole_page_is_markdown'),
    url(r'^pgwithmd$', views.page_including_markdown, name='page_including_markdown'),
]



