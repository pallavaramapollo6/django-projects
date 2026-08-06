from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

# This function name "register" should be used in
# action="register" in form tag of home.html
def register(request):
    name = request.POST['name']
    password = request.POST['password']
    address = request.POST['address']
    mail = request.POST['mail']
    return render(
        request,'output.html',
        # Below dictionary keys should match output.html {{format}}
        # Below dictionary values should be variables declared above
        {'Name':name,'password':password,'address':address,'mail':mail}
    )
