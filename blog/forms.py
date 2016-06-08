from django import forms
from .models import Category, Shop, Review

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['comment', 'photo']