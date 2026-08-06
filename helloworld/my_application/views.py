from django.http import HttpResponse

# Create your views here
def home(request):
    msg = "<h1> Welcome to home page <h1>"
    return HttpResponse(msg)
