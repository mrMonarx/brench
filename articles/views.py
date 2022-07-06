from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

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

@login_required
def create_view_old(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        print(title,content)
        Article.objects.create(title=title, content=content)
        context['form'] = ArticleForm()
        return redirect(to='/')
    return render(request=request, template_name='articles/create.html', context=context)

@login_required
def create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        form.save()
        context['form'] = ArticleForm()
        return redirect(to='/')
    return render(request=request, template_name='articles/create.html', context=context)