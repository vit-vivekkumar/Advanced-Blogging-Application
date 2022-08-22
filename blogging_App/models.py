from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.defaultfilters import default, slugify
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts',blank=True,null=True)
	slug = models.SlugField(max_length=200, unique=True,help_text="Slug is a field in autocomplete mode, but if you want you can modify its contents")
	upload = models.ImageField(upload_to ='imgages/',blank=True,null=True, help_text="Upload a Picture for title Image.",default='uploads/925667.jpg')
	updated_on = models.DateTimeField(auto_now= True)
	content = RichTextField()
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS, default=0)
	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80,null=True)
    email = models.EmailField(null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)