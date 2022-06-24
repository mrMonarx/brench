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
    # title = obj.title
    # content = obj.content

    content = {'title': obj.title,
               'id': obj.id,
               'content': obj.content}


    HTML_STRING = render_to_string(template_name='my_footer.html', context=content)
    return HttpResponse(HTML_STRING)


