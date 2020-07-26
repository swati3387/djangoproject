from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    #return HttpResponse("<b>Here's the text of the Web page.</b>")
    posts= Post.objects.all()
    context={"posts": posts}
    return render(request,'blog/post_list.html',context)
def post_detail(request, pk):
    #return HttpResponse("<b>Here's the text of the Web page.</b>")
    post= get_object_or_404(Post,pk=pk)
    context={"post": post}
    return render(request,'blog/post_detail.html',context)

