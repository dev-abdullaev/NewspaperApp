from .models import Articles
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.urls import reverse_lazy


class ArticleListView(ListView):
    model = Articles
    template_name = "article_list.html"
    context_object_name = "articles"
    login_url = "login"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = "article_detail.html"
    context_object_name = "article"
    login_url = "login"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = "article_create.html"
    fields = ("title", "body")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ("title", "body")
    template_name = "article_edit.html"
    login_url = "login"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
