from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Author
from .forms import AuthorForm,CreateUserForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User

from django.urls import reverse

def AdminRegister(request):

    if request.user.is_authenticated != True:    
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                admin_grup = Group.objects.get(name="admin")
                user.groups.add(admin_grup)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                Author.objects.create(user=user,name=user.username,email=user.email)
                return redirect('login')
        context = {"form":form,"formname":"admin"}
        return render(request,'register.html',context)
    else:
        return HttpResponse("cannot register page")



def Register(request):
    if request.user.is_authenticated != True:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                author_grup = Group.objects.get(name="author")
                user.groups.add(author_grup)
                Author.objects.create(user=user,name=user.username,email=user.email)
                return redirect('login')
        context = {"form":form,"formname":"author"}
        return render(request,'register.html',context)
    else:
        return HttpResponse("cannot register page")

def Login(request):
    if request.user.is_authenticated != True:

        form = LoginForm()
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                name = User.objects.get(id=request.user.id)
                
                for groupfetch in name.groups.all():
                    
                    if (str(groupfetch) == "author"):
                        groupname = groupfetch

                    elif(str(groupfetch)=="admin"):
                        groupname = groupfetch

                print("groupname: ",groupname)
                if str(groupname) == "author":
                    url = reverse('viewauthor',args={user.id})
                    return redirect(url)
                
                elif str(groupname) == "admin":
                    return redirect('home')
                
                else:
                    return HttpResponse("error loading")
        return render(request,"login.html",context={"form":form})
    else:
        return HttpResponse("cannot register page")


def LogoutPage(request):
    logout(request)
    return redirect('login')

def UserPage(request):
    if request.user.is_authenticated and request.user.is_superuser:

        author = Author.objects.all()
        # for authors in author:
            # if authors.profile != None:
                # print("authors profile",authors.profile)
        forms = AuthorForm()
        context = {"forms":forms,"authors":author}
        return render(request,'home.html',context=context)
    elif(request.user.is_authenticated):
        url = reverse('viewauthor',args={request.user.author.id})
        return redirect(url)
    else:
        return redirect('login')
    
def createAuthor(request):
    if request.user.is_authenticated:

        form = AuthorForm()
        formname = "Author create form"
        if request.method == "POST":
            form = AuthorForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                form = AuthorForm()
        context = {"form":form,"formname":formname}
        return render(request,"authorform.html",context)
    else:
        return HttpResponse("ypu are unautorized to view this page")

def viewAuthor(request,pk):
    if request.user.is_authenticated:
        author = Author.objects.get(id=pk)
        post = author.post_set.all()
        context = {'author':author,'posts':post}
        return render(request,"view.html",context)
    else:
        return HttpResponse("ypu are unautorized to view this page")


def updateAuthor(request,pk):
    if request.user.is_authenticated:
        author = Author.objects.get(id=pk)
        formname = "Author create form"
        form = AuthorForm(instance=author)
        if request.method == "POST":
            form = AuthorForm(request.POST,request.FILES,instance=author)
            if form.is_valid():
                form.save()
                name = User.objects.get(id=request.user.id)
            
                for groupfetch in name.groups.all():
                
                    if (str(groupfetch) == "author"):
                        groupname = groupfetch

                    elif(str(groupfetch)=="admin"):
                        groupname = groupfetch

                if str(groupname) == "author":
                    url = reverse('viewauthor',args={request.user.author.id})
                    return redirect(url)
            
                elif str(groupname) == "admin":
                    return redirect('home')
            
                else:
                    return HttpResponse("error loading")
                
        context = {"form":form,"formname":formname}
        return render(request,"authorform.html",context)
    else:
        return HttpResponse("ypu are unautorized to view this page")


def deleteAuthor(request,pk):
    if request.user.is_authenticated:
        author = Author.objects.get(id=pk)

        if request.method == "POST":
            author.delete()
            return redirect('home')
        context = {"pk":pk}
        return render(request,"delete.html",context)
    else:
        return HttpResponse("ypu are unautorized to view this page")
    

def successPage(request):
    return render(request,'success.html')

def deletePage(request):
    return render(request,'delete.html')