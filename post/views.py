from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, PostImageForm
from .models import Post, PostImage

# Create your views here.

def write(request):
    if request.method =='POST':
        title=request.POST.get('title')
        text=request.POST.get('text')
        
        post=Post.objects.create(
            title=title,
            text=text
        )
        images = request.FILES.getlist('image')
        for img in images:
            PostImage.objects.create(post=post, image=img)
            #images = request.FILES.getlist('image')
            
        return redirect('main')
    else:
        return render(request, 'write.html')
    

def main(request):
    posts=Post.objects.all().order_by('-id')

    return render(request, 'main.html', {'posts':posts})

def detail(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    images = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {'post':post, 'images': images})
