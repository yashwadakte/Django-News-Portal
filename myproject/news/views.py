from django.shortcuts import render, get_object_or_404
from .models import News, Category


def home(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')

    news = News.objects.all().order_by('-created_at')

    if category_id:
        news = news.filter(category_id=category_id)

    if query:
        news = news.filter(title__icontains=query)

    categories = Category.objects.all()

    return render(request, 'news/home.html', {
        'news': news,
        'categories': categories
    })


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'news/detail.html', {'news': news})