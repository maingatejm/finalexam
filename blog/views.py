from django.shortcuts import render, redirect
from .models import Category, Shop, Review

def index(request):
	category_list = Category.objects.all()
	review_list = Review.objects.all()
	return render(request, 'blog/index.html', {'category_list' : category_list, 'review_list':review_list,})

def category_detail(request, c_pk):
	category = Category.objects.get(pk=c_pk)
	shop_list = Shop.objects.all().filter(category=category)
	return render(request, 'blog/category_detail.html', {'category':category, 'shop_list':shop_list})


def shop_detail(request, c_pk, s_pk):
	shop= Shop.obejects.get(pk=s_pk)
	review_list = Review.obejects.all().fileter(shop=shop)
	return render(request, 'blog/shop_detail.html', {'shop':shop, 'review_list':review_list})