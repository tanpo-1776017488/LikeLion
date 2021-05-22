from django.db import models


class Blog(models.Model): #id column은 models.Model에 있어서 따로 선언 x
    title=models.CharField(max_length=200)
    writer=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()
    img=models.ImageField(upload_to='blog/',blank=True,null=True)
    #image field를 사용하려면 pillow반드시 필요함
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    

    

