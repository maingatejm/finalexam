from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<c_pk>\d+)/$', views.category_detail, name='category_detail'),
	url(r'^(?P<c_pk>\d+)/shop/(?P<s_pk>\d+)/$', views.shop_detail, name='shop_detail'),
]