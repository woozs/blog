from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType

# Create your views here.


def blog_list(requset):
    context ={}
    context['blogs'] = Blog.objects.all()
    context['blogs_count'] = Blog.objects.all().count()
    context['blog_types'] = BlogType.objects.all()
    return  render_to_response('blog/blog_list.html', context)



def blog_detail(requset,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    return render_to_response('blog/blog_detail.html', context)


def blogs_with_type(requset,type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response('blog/blogs_with_type.html', context)





