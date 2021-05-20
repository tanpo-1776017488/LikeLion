from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
def home(request):
    blogs=Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request,id):
    blog=get_object_or_404(Blog,pk=id)# argument : class , PK 
    return render(request,'detail.html',{'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request): 
    new_blog=Blog()
    new_blog.title=request.POST['title']
    new_blog.writer=request.POST['writer']
    new_blog.body=request.POST['body']
    new_blog.pub_date=timezone.now() #현재 시각을 기준으로 생성
    new_blog.save() #database에 저장
    return redirect('detail',new_blog.id) #새로 만든 글의 detail