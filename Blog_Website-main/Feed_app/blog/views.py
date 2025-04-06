from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Post

# def home(request):
# 	return HttpResponse('<h1>Blog Home</h1>')
# context = {
# 		'posts': posts
# 	}
# 	return render(request,'blog/home.html',context)



# def about(request):
# 	return HttpResponse('<h1>About Blog</h1>')

# posts =[
# {
# 	'author':'Kalpana',
# 	'title':'Learn the way you like',
# 	'content':'Be specilaized in a thing you love to do.',
# 	'date_posted':'November 6,2024'
# },
# {
# 	'author':'Devi',
# 	'title':'Django',
# 	'content':'Django tutorial by corey schafer',
# 	'date_posted':'November 1,2024'
# }

# ]  


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request,'blog/home.html',context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields =['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields =['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model = Post
	success_url ='/'

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request,'blog/about.html',{'title':'About'})