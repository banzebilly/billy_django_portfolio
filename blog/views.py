from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import BlogProject

# Create your views here.



def blog_home(request):
    blogs = BlogProject.objects.all().order_by('created_at')
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blog_home.html', context)



def blog_detail(request, pk):
    blog = get_object_or_404(BlogProject, pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blogs/blog_detail.html', context)  


def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_blog')
        else:
            return ( form.error)
    else:
        form = BlogForm()

    context = {
        'form': form,
    }
    
    return render(request, 'blogs/blog_post.html', context)