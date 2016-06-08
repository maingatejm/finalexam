from django.shortcuts import render, redirect,get_object_or_404
from .models import Category, Shop, Review
from .forms import CategoryForm, ReviewForm, ShopForm
from django.contrib.auth.decorators import login_required

def index(request):
	category_list = Category.objects.all()
	review_list = Review.objects.all()
	return render(request, 'blog/index.html', {'category_list' : category_list, 'review_list':review_list,})

def category_detail(request, c_pk):
	category = Category.objects.get(pk=c_pk)
	shop_list = Shop.objects.all().filter(category=category)
	return render(request, 'blog/category_detail.html', {'category':category, 'shop_list':shop_list})


def shop_detail(request, c_pk, s_pk):
	category = Category.objects.get(pk=c_pk)
	shop = Shop.objects.get(pk=s_pk, category = category)
	review_list = Review.objects.all().filter(shop=shop)
	return render(request, 'blog/shop_detail.html', {'shop':shop, 'review_list':review_list})

@login_required
def category_new(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog:index')
	else : 
		form = CategoryForm()
	return render(request, 'blog/category_form.html', {'form':form,})

@login_required
def category_edit(request, c_pk):
	category = get_object_or_404(Category, pk = c_pk)
	if request.method == 'POST':
			form = CategoryForm(request.POST, instance=category)
			if form.is_valid():
				form.save()

			return redirect('blog:category_detail', c_pk)
	else:
			form = CategoryForm(instance=category)
	return render(request,'blog/category_form.html', {'form':form,})

@login_required
def review_new(request,c_pk, s_pk):
	if request.method == "POST":
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.save(commit=False)
			review.shop = get_object_or_404(Shop, pk=s_pk)
			review.user = request.user
			review.save()
			
			return redirect('blog:shop_detail', c_pk, s_pk)
	else : 
		form = ReviewForm()
	return render(request, 'blog/review_form.html', {'form':form,})

@login_required
def review_edit(request, c_pk, s_pk, pk):
	review = get_object_or_404(Review, pk = pk)
	if request.method == 'POST':
			form = ReviewForm(request.POST, instance=review)
			if form.is_valid():
				review = form.save(commit=False)
				review.shop = get_object_or_404(Shop, pk=s_pk)
				review.user = request.user
				review.save()

			return redirect('blog:shop_detail', c_pk, s_pk)
	else:
			form = ReviewForm(instance=review)
	return render(request,'blog/review_form.html', {'form':form,})

@login_required
def shop_new(request,c_pk):
	if request.method == "POST":
		form = ShopForm(request.POST)
		if form.is_valid():
			shop = form.save(commit=False)
			shop.category = get_object_or_404(Category, pk=c_pk)
			shop.save()
			
			return redirect('blog:category_detail', c_pk)
	else : 
		form = ShopForm()
	return render(request, 'blog/shop_form.html', {'form':form,})

@login_required
def shop_edit(request, c_pk, s_pk):
	review = get_object_or_404(Review, pk = pk)
	if request.method == 'POST':
			form = ReviewForm(request.POST, instance=review)
			if form.is_valid():
				review = form.save(commit=False)
				review.shop = get_object_or_404(Shop, pk=s_pk)
				review.user = request.user
				review.save()

			return redirect('blog:shop_detail', c_pk, s_pk)
	else:
			form = ReviewForm(instance=review)
	return render(request,'blog/review_form.html', {'form':form,})
