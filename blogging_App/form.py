
from .models import Comment
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Post

# class PostAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
	
#     class Meta:
#         model = Post

# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets={
            'name':forms.TextInput(),
            'email':forms.TextInput(),
            'body':forms.Textarea(attrs={"class":"form-control"}),
        }
