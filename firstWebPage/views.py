from django.http import HttpResponse
from django.utils import timezone
from random import randint



def home(request):
    name = 'Django'
    number = randint(1,100)
    date = timezone.now()
    # databae =
    # title =
    # content = 
    H1_STRING = f"""<h1>Hello {name},Time:{date}</h1>"""
    P_STRING = f"""<p>Hello {number}</p>"""
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)


