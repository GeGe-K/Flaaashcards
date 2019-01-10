from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^accounts/profile/',views.profile, name='profile'),
    url(r'^delete_card/(\d+)', views.delete_card ,name='delete'),
    url(r'^post_card/',views.post_card, name='post'),
    url(r'^update_card/',views.update_card, name='update'),
]