#from django.conf.urls import url
#from . import views

#urlpatterns = [
#    url(r'^$', views.index, name='index')]
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),

                url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(
                                    model = Post,
                                    template_name="blog/post.html")),
                #url(r'^dashboard/', ListView.as_view(
                #                    queryset=Post.objects.filter(title='Post by Dumm2').order_by("-date")[:25],
                #                    template_name="blog/blog.html")),
                url(r'^dashboard/',views.dashboard,name='dashboard'),
      
            ]