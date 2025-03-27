from django import forms
from blogs.models import Post, Category, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']