from django.http import HttpResponse
from django.utils import timezone
from random import randint

from articles.models import Article



def home(request):
    name = 'Django'
    number = randint(1,2)
    date = timezone.now()
    # database =
    obj = Article.objects.get(id=number)
    title = obj.title
    content = obj.content
    H1_STRING = f"""<h1>Hello {title} ,({number}) </h1>"""
    P_STRING = f"""<p>Hello {content}</p>"""
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)


