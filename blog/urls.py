from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
]

#a href ="{url blog:post_list}"
