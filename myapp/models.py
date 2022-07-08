from django.db import models

# Create your models here.

class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	remarks=models.TextField()

	def __str__(self):
		return self.name

class user(models.Model):
	uname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	remarks=models.TextField()

	def __str__(self):
		return self.uname