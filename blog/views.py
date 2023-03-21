from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post


# Create your views here.
# def post_list(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
        }
    )
