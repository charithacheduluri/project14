from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'charitha'}
    return render(request,'looping.html',d)