from django.shortcuts import render
from django.shortcuts import HttpResponse
def showMain(request):
    return render(request,"inex.html")
def newDetails(request):
    return render(request,"new.html")
def viewDetails(request):
    return render(request,"view.html")
def saveDetails(request):
    id=request.POST.get("idno")
    na=request.POST.get("name")
    sal=request.POST.get("salary")
    doj=request.POST.get("doj")
    return HttpResponse(id+na+sal+doj)