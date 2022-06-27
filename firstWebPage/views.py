from django.http import HttpResponse
from django.utils import timezone
from random import randint

from articles.models import Article
from django.template.loader import render_to_string


def home(request):
    name = 'Django'
    number = randint(1,3)
    date = timezone.now()
    # database =
    obj = Article.objects.get(id=number)
    # my_list = ['python','django','flask','django rest api','flask api','c++','c#','go']
    # title = obj.title
    # content = obj.content

    objects = Article.objects.all()

    content = {'title': obj.title,
               'id': obj.id,
               'content': obj.content,
               # 'my_list': my_list,
               'objects': objects}


    HTML_STRING = render_to_string(template_name='home.html', context=content)
    return HttpResponse(HTML_STRING)


