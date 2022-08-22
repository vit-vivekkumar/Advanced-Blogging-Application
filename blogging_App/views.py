from .form import CommentForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView

from django.views import generic
from .models import Post


# home
def index(request):
   
    return render(request,'index.html')

# dashboard
def dashboard(request):
    try:
        if request.user.is_authenticated:
            post_list = Post.objects.filter(author=request.user)
            darft_post = Post.objects.filter(status=0).order_by('-created_on')
            darft=darft_post.count()
            count=post_list.count()
        else:
            pass
    except ObjectDoesNotExist:
        pass

    context={
            'post_list':post_list,
            'count':count,
            'darft':darft,
        }
    return render(request,'dashboard/dashboard.html',context)

def profile(request):
   
    return render(request,'dashboard/user.html')

class addpost(generic.CreateView):
    model=Post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(addpost, self).form_valid(form)

    template_name='dashboard/addpost.html'
    fields=('title','upload','slug','content','status')

class updatepost(generic.UpdateView):
    model=Post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    template_name='dashboard/addpost.html'
    fields=('title','upload','slug','content','status')

class deletepost(generic.DeleteView): 
    model=Post
    template_name='dashboard/post_confirm_delete.html'
    success_url=reverse_lazy('home')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def PostDetail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

# home
def support(request):
    return render(request,'support.html')