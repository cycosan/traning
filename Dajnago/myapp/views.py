from django.shortcuts import render
from django.http import HttpResponse
from myapp import models
from myapp import forms
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
def addcomment(request):
    has_commented=request.session.get("has_commented")
    if(not has_commented):
        request.session["has_commented"]=True
        # username=request.POST.get("username")
        # content=request.POST.get("content")
        # c=models.Comments(username=username,content=content)
        f=forms.CommentForm(request.POST)
        f.save()
        comments = models.Comments.objects.all()
        commeted = {
            "comments": comments
        }
        return render(request, 'myapp/viewComment.html', d)
    else:
        return HttpResponse("You have already commeted")
def index(request):
    return render(request,'myapp/someform.html')
# def showcomments(request):
#     d={
#         "comments":
#        You have already commeted [
#             {"username":"hey",
#             "content":'hello'
#              },[
#             {"username": "hey",
#              "content": 'hello'
#              },
#             {"username": "hey",
#              "content": 'hello'
#              },
#
#         ]
#     }
#     return render(request,'myapp/viewComment.html',d)
def showcomments(request):
    comments=models.Comments.objects.all()
    d={
      "comments":comments
    }
    return render(request, 'myapp/viewComment.html', d)


def delcommments(request):
    comment_id=request.POST.get("comment_id")
    models.Comments.objects.filter(pk=comment_id).delete()
    comments = models.Comments.objects.all()
    d = {
        "comments": comments
    }
    return render(request, 'myapp/viewComment.html', d)

def login(request):

    f=forms.LoginForm()
    return render(request,'myapp/login.html',{'form':f})