from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from apps.post.models import Post, Comment
from apps.post.forms import PostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.views.generic.list import ListView
from django.db import transaction

# Create your views here.
def index(request):
    return render(request, "post/index.html")


@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    template_name = "post/create_post.html"
    form_class = PostForm
    # login_url = "accounts/create"

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.slug = slugify(self.object.title)
        self.object.save()
        return redirect(self.get_success_url())


class PostDetailView(DetailView):
    model = Post
    template_name = "post/details.html"

    def get_context_data(self,  **kwargs):
        # content["comments"] = Comment.objects.filter(post="")
        # return content
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=1)
        return context



class PostListView(ListView):
    model = Post
    template_name = "post/list.html"

@transaction.atomic
def create_comment(request, id):
    commented_by = request.user
    data = request.data
    comment_data = data.get("comment")
    comment = Comment.objects.create(post=id, commented_by=commented_by, comment=comment_data)
    return comment
