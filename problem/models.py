from django.db import models

# Create your models here.


class total(models.Model):
	title = models.CharField(max_length=200)
	problem = models.CharField(max_length=200)
	link = models.CharField(max_length=200)


class easy(models.Model):
	title = models.CharField(max_length=200)
	problem = models.CharField(max_length=200)
	link = models.CharField(max_length=200)


class medium(models.Model):
	title = models.CharField(max_length=200)
	problem = models.CharField(max_length=200)
	link = models.CharField(max_length=200)

class hard(models.Model):
	title = models.CharField(max_length=200)
	problem = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
