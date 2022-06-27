from django.shortcuts import render
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
