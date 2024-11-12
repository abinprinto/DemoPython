from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from . models import Place,Person
# Create your views here.

# def demo(request):
#     name="india"
#     return render(request, "home.html",{'obj':name})
# def about(request):
#     return render(request,"result.html")
#
# def contact(request):
#     return HttpResponse("Hello this is contact")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     rem=x%y
#     return render(request,"result.html",{'add':add,'sub':sub,'mul':mul,'div':div,'rem':rem})
def demo(request):
    obj = Place.objects.all()  # Get all Place objects
    person = Person.objects.all()  # Get all Person objects
    return render(request, "index.html", {'result':obj, 'person': person})


