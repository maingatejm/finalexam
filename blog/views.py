from django.shortcuts import render, redirect,get_object_or_404
from .models import Category, Shop, Review
from .forms import CategoryForm

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
	shop = Category.objects.get(pk=s_pk).filter(category=category)
	review_list = Review.obejects.all().fileter(shop=shop)
	return render(request, 'blog/shop_detail.html', {'shop':shop, 'review_list':review_list})

def category_new(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog:index')
	else : 
		form = CategoryForm()
	return render(request, 'blog/category_form.html', {'form':form,})

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



