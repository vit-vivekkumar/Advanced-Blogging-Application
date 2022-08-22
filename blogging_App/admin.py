from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on','upload','author')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

# class MyAdmin(admin.ModelAdmin):
#     def save_model(self, request, instance, form, change):
#         user = request.user 
#         instance = form.save(commit=False)
#         if not change or not instance.author:
#             instance.author = user
#         instance.modified_by = user
#         instance.save()
#         form.save_m2m()
#         return instance



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

        
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)