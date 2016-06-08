from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<c_pk>\d+)/$', views.category_detail, name='category_detail'),
	url(r'^(?P<c_pk>\d+)/shop/(?P<s_pk>\d+)/$', views.shop_detail, name='shop_detail'),
	url(r'^category/new/$', views.category_new, name="category_new"),
	url(r'^category/(?P<c_pk>\d+)/edit/$', views.category_edit, name='category_edit'),
	url(r'^(?P<c_pk>\d+)/shop/(?P<s_pk>\d+)/review/new/$', views.review_new, name='review_new'),
	url(r'^(?P<c_pk>\d+)/shop/(?P<s_pk>\d+)/review/(?P<pk>\d+)/edit/$', views.review_edit, name='review_edit'),
	url(r'^(?P<c_pk>\d+)/shop/new/$', views.shop_new, name='shop_new'),
	url(r'^(?P<c_pk>\d+)/shop/(?P<s_pk>\d+)/edit/$', views.shop_edit, name='shop_edit'),
]
