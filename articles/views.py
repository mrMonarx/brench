from django.shortcuts import render,redirect
from .models import Article


# Create your views here.

def detail_view(request, id):
    obj = None
    if id is not None:
        obj = Article.objects.get(id=id)

    context = {
        'object': obj,
    }

    return render(request=request, template_name='articles/detail.html', context=context)

def search_view(request):
    try:
        pk = int(request.GET.get('q'))
    except:
        pk = None

    obj = None

    if pk is not None:
        try:
            obj = Article.objects.get(id=pk)
        except:
            obj = None

    contect = {
        'object': obj
    }

    return render(request=request, template_name='articles/search.html', context=contect)

def create_view(request):
    post = request.method
    if post == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Article.objects.create(title=title,content=content)
            return redirect(to='http://127.0.0.1:8000/')
    return render(request=request, template_name='articles/create.html')