from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from blog.models import Blog, Category, Movies
from django.core.files.storage import FileSystemStorage
from .forms import MovieForm





def index(request):
    
    context = {
        "blogs": Blog.objects.filter(is_home=True,is_active=True),
        "categories":Category.objects.all()
    }
    return render(request, "blog/index.html",context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories":Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blogs_details(request, slug):
    
    blog= Blog.objects.get(slug=slug)
    return render(request, "blog/blogs_details.html",{
        "blog":blog
    })
        
    
def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        #"blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories":Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)

def upload(request):
	if request.method == "POST":
		form = MovieForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("upload")
	form = MovieForm()
	movies = Movies.objects.all()
	return render(request=request, template_name="blog/upload.html", context={'form':form, 'movies':movies})