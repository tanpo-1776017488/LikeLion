from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','writer','body','img'] #pub_date는 제외
    