from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User , related_name='profile_user',on_delete=models.CASCADE)
    fname = models.CharField(max_length=1000, null=True)
    lname = models.CharField(max_length=1000, null=True)
    dob = models.DateField(null=True)
    email = models.EmailField(null=True)
    fake_id = models.IntegerField(default=0)
    

    friends = models.ManyToManyField(User )
    

    def __str__(self) :
        return str(self.fname)

class Post(models.Model):
    txt = models.CharField(max_length=100000)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    
    liked = models.ManyToManyField(User , related_name="post_like" )
    
    def total_liked(self):
        return self.liked.count()
    def __str__(self) :
        return self.txt

class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    text = models.CharField(max_length=100000)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    liked = models.ManyToManyField(User , related_name="comment_like" ,  blank=True)

    def __str__(self) :
        return self.text

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        obj = Profile.objects.create(user=instance)
        obj.fake_id = instance.user.id
        obj.save()