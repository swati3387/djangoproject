from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list(request):
    #return HttpResponse("<b>Here's the text of the Web page.</b>")
    context={}
    return render(request,'blog/post_list.html',context)
