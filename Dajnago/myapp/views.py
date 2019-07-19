from django.shortcuts import render
from django.http import HttpResponse
from myapp import models
# Create your views here.
#def index(request):
 #   return HttpResponse("hello World")
def profile(request):
    name=request.GET.get("name")
    skills=["java","pyhton","golang"]
    d={"name":name ,"skills":skills}
    return render(request,'myapp/hello.html',d)
def add(request):
    a=request.GET.get("a")
    b=request.GET.get("b")

    return HttpResponse(int(a)+int(b))
def submit(request):
    username=request.POST.get("username")
    comment=request.POST.get("comment")
    commentModel=models.Comments(username=username,content=comment)
    commentModel.save()
    commentList=models.Comments.objects.all()
    for i in commentList:
        print(i)
    skills = ["java", "pyhton", "golang"]
    d = {"name":username, "skills": skills,"comment":comment}
    return render(request, 'myapp/hello.html', d)
def index(request):
    return render(request,'myapp/someform.html')