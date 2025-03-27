from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blogs.models import Post, Category, Comment
from blogs.forms import UserRegistrationForm, PostCreateForm, CommentForm
from django.urls import reverse_lazy

def post_list(request):
    posts = Post.objects.all().order_by('-create_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments  = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect(reverse_lazy('post_detail', kwargs={'pk': post.pk}))
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post, 
        'comments': comments, 
        'comment_form': comment_form
    }
    return render(request, 'post_detail.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form .save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Poss successfully created')
            return redirect(reverse_lazy('post_list'))
    else:
        form = PostCreateForm()
    
    return render(request, 'create_post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}!')
            return redirect(reverse_lazy('login'))
    else:    
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



