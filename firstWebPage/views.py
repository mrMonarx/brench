from django.http import HttpResponse

Home_Web_View = """Python is the best programming language"""


def home(request):
    print(Home_Web_View)
    return HttpResponse(Home_Web_View)
