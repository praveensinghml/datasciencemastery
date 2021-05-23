from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from posts.models import Author,Comment,Activity,Post, PostView
@receiver(post_save, sender=User)
def user_as_author(sender,created,instance, **kwargs):
    if created:
        Author.objects.create(user=instance)
@receiver(post_save, sender=Comment)
def get_comment_activity(sender,created,instance, **kwargs):
    if created:
        Activity.objects.create(Activity_name="comment",Activity_message=instance.content,created_by=instance.user,post=instance.post,user=instance.post.author.user)    
@receiver(post_save, sender=Post)            
def get_post_activity(sender,created,instance, **kwargs):
    if created:
        Activity.objects.create(Activity_name="Post",Activity_message=instance.title,created_by=instance.author.user,post=Post.objects.get(id=instance.id),user=instance.author.user)        
    else:
        Activity.objects.create(Activity_name="vote",Activity_message="votes",created_by=instance.author.user,post=Post.objects.get(id=instance.id),user=instance.author.user)

@receiver(post_save, sender=PostView)
def get_comment_activity(sender,created,instance, **kwargs):
    if created:
        Activity.objects.create(Activity_name="view",Activity_message="some one views",created_by=instance.user,post=instance.post,user=instance.post.author.user)    
