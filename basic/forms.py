from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django.forms import ModelForm


class NewPost(ModelForm):
    class Meta:
        models = Post
        fields = "__all__"
class NewUser(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username'  , 'password1' , 'password2' ,'email']