from django.db import models
from django.conf import settings

class Category(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Shop(models.Model):
	category = models.ForeignKey(Category)
	shop_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)
	address = models.TextField()
	message = models.TextField()
	photo1 = models.ImageField()
	photo2 = models.ImageField(null=True, blank=True)
	photo3 = models.ImageField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.shop_name

class Review(models.Model):
	shop = models.ForeignKey(Shop)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	comment = models.TextField()
	photo = models.ImageField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)




