from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "news/article_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        queryset = Article.objects.filter(is_published=True)
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset.order_by("-created_at")


class ArticleDetailView(DetailView):
    model = Article
    template_name = "news/article_detail.html"
    context_object_name = "article"
