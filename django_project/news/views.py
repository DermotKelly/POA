from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm

def news_list(request):
    news_articles = News.objects.order_by('-pub_date')
    return render(request, 'news/news_list.html', {'news_articles': news_articles})

def news_detail(request, news_id):
    news_article = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news_article': news_article})

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})
