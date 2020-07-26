from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    #return HttpResponse("<b>Here's the text of the Web page.</b>")
    posts= Post.objects.all()
    context={"posts": posts}
    return render(request,'blog/post_list.html',context)
