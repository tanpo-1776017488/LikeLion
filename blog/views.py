from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
def home(request):
    blogs=Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request,id):
    blog=get_object_or_404(Blog,pk=id)# argument : class , PK 
    return render(request,'detail.html',{'blog':blog})

def new(request):
    form=BlogForm()
    return render(request,'new.html',{'form':form})

def create(request): 
    # new_blog=Blog()
    # new_blog.title=request.POST['title']
    # new_blog.writer=request.POST['writer']
    # new_blog.body=request.POST['body']
    # new_blog.img=request.FILES['image']
    # new_blog.pub_date=timezone.now() #현재 시각을 기준으로 생성
    # new_blog.save() #database에 저장
    form=BlogForm(request.POST,request.FILES)
    if form.is_valid():
        new_blog=form.save(commit=False)
        new_blog.pub_date=timezone.now()
        new_blog.save()
        return redirect('detail',new_blog.id) #새로 만든 글의 detail
    return redirect('home')
    
def edit(request,id):
    edit_blog=Blog.objects.get(id=id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id):
    update_blog=Blog.objects.get(id=id)
    update_blog.title=request.POST['title']
    update_blog.writer=request.POST['writer']
    update_blog.body=request.POST['body']
    update_blog.pub_date=timezone.now() #현재 시각을 기준으로 생성
    update_blog.save() #database에 저장
    return redirect('detail',update_blog.id)

def delete(request,id):
    delete_blog=Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')