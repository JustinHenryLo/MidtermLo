from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Comment
from .forms import PostModelForm,CommentModelForm
from datetime import datetime 

# Create your views here.
def index(request):
    context = {} #params
    post = Post.objects.all()
    context['post']=post
    return render(request,"index.html",context)

def detail(request,post_id):
    context={}
    post = Post.objects.get(id=post_id)
    context['post'] = post
    return render(request,"detail.html",context)


def comment(request,post_id):
    context={}
    if(request.method == 'POST'):
        form = CommentModelForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('post:detail',post_id)
        else:
            context['comment_form']=form
            return render(request,'comment.html',context)
    else:
        post = Post.objects.get(id=post_id)
        form = CommentModelForm(initial = {'question':post,'date_created':datetime.now()})
        context['comment_form']=form
        context['post_id']=post_id
        return render(request,'comment.html',context)

def create(request):
    context={}
    if(request.method == 'POST'):
        form = PostModelForm(request.POST)
        if(form.is_valid()):
            form.save()#this fucking returns the object it saves !!!!!!!!!!
            return redirect('post:index')
        else:
            context['post_form']=form
            return render(request,'create.html',context)
    else:
        form = PostModelForm()
        context['post_form']=form
        return render(request,'create.html',context)

def update(request,post_id):
    context ={}
    post = Post.objects.get(id=post_id)
    if(request.method == 'POST'):
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():  #data val
            form.save()
            return redirect('post:detail',post_id)
        else:
            context['form']=form
            return render(request,'update.html',context)
       
    else:
        context['form'] =PostModelForm(instance=post)
        return render(request,"update.html",context)