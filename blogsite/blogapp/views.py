from typing import Any, Dict
from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from .forms import *
import math ,random
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash,authenticate
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from AuthApp.models import *
from AuthApp.forms import UserProfileUpdate ,CustomUserDataForm
from django.views.generic.base import *
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from django.urls import reverse_lazy
from django.http import HttpResponse 
from xhtml2pdf import pisa


# Create your views here.

# Create your views here.



def read(request):
    read_data = blog.objects.all()
    LikeBlog =  Like.objects.all()
    if request.user in read_data:
        done = 1
    else: 
        done = 0
    
    paginator = Paginator(read_data, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
  
    
    return render(request,'home.html',{'read_data':page_obj , 'done':done , })





# def home(request):
#     if request.user.is_authenticated:
#         data = tut.objects.all()
#         paginator = Paginator(data, 6)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         return render(request, 'home.html', {'data': page_obj})
#     else:
#         return render(request, 'home.html',)


def create(request):
    if request.method == 'GET':
        form = blogform()
        return render(request,'create.html',{'form':form})
    else:
        form = blogform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home'  )
        else:
            messages.info(request , form.errors)
            return redirect('create' ,)


def update(request,id):
    if request.method =='GET':
        data = blog.objects.get(id=id)
        form = blogform(instance=data)
        return render(request,'create.html',{'form':form})
    else:
        data = blog.objects.get(id=id)
        form = blogform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')


def delete(request,id):
    del_data = blog.objects.get(id=id)
    del_data.delete()
    return redirect('home')

    







def search(request):
    inp_search = request.POST['QuerieS']
    print(inp_search)
    read_data = blog.objects.filter(heading__icontains = inp_search)
    paginator = Paginator(read_data, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'Blog':page_obj})


def first(request):
    return render(request,'first.html')



def CurrentUserProfile(request ):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(id=request.user.id)
        Blogs = blog.objects.filter(upload_by__exact = user)
        BlogCount = Blogs.count()
           
        return render(request,'Profiles.html' , {'user':user ,'BlogCount':BlogCount , 'Blogs':Blogs})
        
        
    else:
        return redirect('login')
        
def CurrentUserProfileUpdate(request):
    if request.method == "GET":
        form = UserProfileUpdate()
        User = request.user
        return render(request , 'UserProfileUpdate.html' , {'form':form , 'User':User})
    else:
        form = UserProfileUpdate(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('CurrentUserProfile')
        else:
            messages.error(request , form.errors)
            return redirect('CurrentUserProfileUpdate')

def UserDataupdate(request):
    if request.method == "GET":
        user = request.user
        form = CustomUserDataForm(instance=user)
        return render(request , 'UpdateUser.html' ,{'form':form})
    else:
        form = CustomUserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CurrentUserProfile')
        else:
            messages.error(request, form.errors)
            return render(request , 'UpdateUser.html' )
        

def Categories(request):
    li = ['https://img.freepik.com/free-vector/vintage-monochrome-skull-pirate-hat_225004-2011.jpg?w=740&t=st=1682749458~exp=1682750058~hmac=9afe5818a9ca506aeb433ce6273739df9124975a851c1003aa8f0944ac68b471' ,'https://mdbootstrap.com/img/new/slides/031.jpg', 'https://mdbootstrap.com/img/new/standard/nature/023.jpg' , 'https://images.unsplash.com/photo-1634840884193-2f6cf2538871?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80'  ]
    AllCategories = tag.objects.all()
    RandomNumber = random.randint(0 ,len(li))
    RandomNumber2 = random.randint(0 ,len(li))
    for i in AllCategories:
        blogimage = blog.objects.filter(tag__title__icontains = i)
        
    AllCategorieslist = zip(AllCategories,li)
    context = {
        'AllCategories':AllCategorieslist,
    }
    return render(request , 'cat.html' , context)

def CategoryBlog(request,tag):
    Blogs = blog.objects.filter(tag__title__icontains = tag)
    return render(request , 'Categoriees.html' , {'Blogs':Blogs ,'tag':tag})

def Likes(request,id):
    if request.user.is_authenticated:
        BlogId = get_object_or_404(blog , id=id)
        like,created = Like.objects.get_or_create( user = request.user , blog = BlogId )
        print(BlogId)
        
        if not created:
            print("Deleting Like")
            like.delete()
            BlogId.likes -= 1
            print("Delete Created")
        else:
            BlogId.likes += 1
            print("Like Created")
            
        BlogId.save()
        return redirect( 'home' )
    else:
        messages.info( request , 'You Should Login before like The Post')
        return redirect( 'home' ,)

# @csrf_exempt
# class CommentsViewT(View):
#     template_name = 'readmore.html'
#     def get(self , request , id , *args , **kwargs ):
#         BlogId = blog.objects.get(id=id)
#         comnt = Comments.objects.all()
#         print(comnt, "Comments")
        
#         form =  CommentForm()
#         print(form)
#         context = {
#           'form': form,
#           'readmore':BlogId
#         }
#         return render(request,self.template_name , context)
    
#     def post(self , request , id , *args , **kwargs):
#         if request.user.is_authenticated:
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('readmore')
#             else:
#                 form = CommentForm()
#                 context = {
#                     'form':form
#                 }
#                 return redirect('readmore')
#         else:
#             messages.error(request , 'You Have To Login To Comment Your Post')
#             return redirect('readmore' , id=id)

# class CommentView(View):
#     template_name = 'readmore.html'
#     def get(self , request , id):
#         Blog = blog.objects.get(id=id)
#         BlogComments  = Comments.objects.filter(blog=Blog)
#         Suncomments = Comments.objects.filter(blog=blog, parent_comment__isnull=True)
#         form = CommentForm()
#         context = {
#             'form':form,
#             'readmore':Blog,
#             'BlogComments':BlogComments,
#             'Suncomments':Suncomments,
#         }
#         return render(request  , self.template_name , context)
    
#     def post(self , request , id):
#         Blog = blog.objects.get(id=id)
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.blog = Blog
#             comment.save()
#             return redirect('Comment' , id=id)
#         else:
#             comments = Comments.objects.filter(blog=Blog)
#             context = {
#                 'form': form,
#                 'blog': Blog,
#                 'comments': comments,
#             }
#             return render(request, 'blog_detail.html', context)
            
class CommentView(View):
    template_name = 'readmore.html'
    
    def get(self, request, id):
        Blog = blog.objects.get(id=id)
        comments = Comments.objects.filter(blog=Blog, )
        form = CommentForm()
        context = {
            'form': form,
            'readmore': Blog,
            'comments': comments,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        if request.user.is_authenticated:
            
            Blog = blog.objects.get(id=id)
            form = CommentForm(request.POST)
        
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.blog = Blog
                
                if 'parent_comment' in form.cleaned_data:
                    parent_comment = Comments.objects.get(id=form.cleaned_data['parent_comment'])
                    comment.parent_comment = parent_comment 
                comment.save()
                updated_comment = Comments.objects.get(id=comment.id)
                return redirect('Comment', id=id)
            else:
                comments = Comments.objects.filter(blog=Blog, parent_comment__isnull=True)
                context = {
                    'form': form,
                    'blog': Blog,
                    'comments': comments,
                    'updated_comment':updated_comment
                }
                return render(request, 'readmore.html', context)
        else:
            messages.error(request ,'You Must login to Comment on Post')
            return redirect('login')
   
     
def CommentDeleteview(request , id):
    Comment = Comments.objects.get(id = id)
    Comment.delete()
    return redirect('home')

def CommentUpdateview(request , id):
    Comment = Comments.objects.get(id=id)
    Blog = Comment.blog
    BlodId = Blog.id
    if request.method == "GET":
        form = CommentUpdateForm(instance = Comment)
        context = {
            'readmore':Blog,
            'form':form,
        }
        return render(request , 'readmore.html'  , context)
    else:
        form = CommentUpdateForm(request.POST , instance=Comment)
        if form.is_valid():
            form.save()
            return redirect('Comment' , BlodId)
        else:
            return redirect("Comment" , form.errors)
            

def ContactView(request ):
    if request.user.is_authenticated:
        if request.method == "POST":
            Firstname = request.POST['Firstname']
            LastName = request.POST['Lastname']
            email = request.POST['email']
            Feedback = request.POST['Feedback']
            username = request.user
            if  not Contact.objects.filter(user_name = username).exists():
                ConatctUser = Contact.objects.create(FirstName = Firstname , LastName = LastName , email = email , Feedback = Feedback , user_name = username )
                ConatctUser.save()
                messages.success(request , 'Your Feedback is Submitted ')
                return redirect('home')
            else:
                messages.info(request , 'You Cannot Give Feedback multiple times')
                return redirect('category')
        else:
            return render(request , 'Categoriess.html' )  
    else:
        messages.info(request , 'Please login First ')
        return redirect('Login')
        
        
        
from django.template.loader import get_template        
def DownloadPdf(request , id):
    Blog = blog.objects.get(id=id)
    template_name = 'data.html'
    print(Blog)
    Context = {'form':Blog}
    
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = f"attachment; filename='{Blog.heading}'.pdf"
    template = get_template(template_name)
    html = template.render(Context)
    pisa_status = pisa.CreatePDF(html , dest = response)
    if pisa_status.err:
        return HttpResponse('Some Error Occured Please Try Again')
    return response