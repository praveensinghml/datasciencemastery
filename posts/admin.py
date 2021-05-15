from django.contrib import admin
from .models import Author, Category, Post, Comment, Tags, PostView,Activity

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tags)
admin.site.register(PostView)
class activity(admin.ModelAdmin):
    list_display=['id','Activity_name','Activity_message','created_by','created_at']
admin.site.register(Activity,activity)    
