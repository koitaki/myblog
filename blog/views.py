from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.

def index(request):
    post_list = Post.objects.order_by('-pub_date')[:25]
    t = get_template('index.html')
    c = Context({'posts': post_list})
    return HttpResponse(t.render(c))


def post_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    context = dict(post=post, comments=comments, form=CommentForm())
    context.update(csrf(request))
    return render(request, 'post.html', context)


def add_comment(request, comment_id):
    p = request.POST
    if 'text' in p and p['text']:
        author = 'Anonymous'
        if p['author']:
            author = p['author']
            comment = Comment(post=Post.objects.get(pk=comment_id))
            cf = CommentForm(p, instance=comment)
            cf.fields['author'].required = False
            comment = cf.save(commit=False)
            comment.author = author
            comment.save()
    return HttpResponseRedirect(reverse('post_page', args=[comment_id]))


def dummy_page(request):
    context = {}
    return render(request, 'dummy.html', context)


def month_timeline():
    year, month = time.localtime()[:2]
