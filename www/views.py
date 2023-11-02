from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articles, Categories, Tags

# pk = primary keys


def CategoryList(request, category_id):
    # aller chercher la categorie demandée
    currentCategory = Categories.objects.get(pk=category_id)
    # aller cherher les articles de la catégorie
    articles = Articles.objects.filter(category=currentCategory)
    # définir un "context" (les infos à afficher)
    context = {
        "title": currentCategory.title,
        "articles": articles,
    }
    # effectuer le "render"
    return render(request, "filters.html", context)


class ArticleList(ListView):
    model = Articles
    template_name = "article_list.html"
    context_object_name = "articles"
    ordering = ["-published_at"]


class ArticleDetail(DetailView):
    model = Articles
    template_name = "article_single.html"
    context_object_name = "article"
