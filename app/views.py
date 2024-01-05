from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'app/base.html',context)

