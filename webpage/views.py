
from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm




# Create your views here.
def homepage(request):
    return render(request,'home.html')

def webpage(request):

    
    prods =Product.objects.all()

    return render(request,'webpage/webpage.html', {'prods': prods})


def search(request):
    form = ProductSearchForm(request.GET)
    prods = Product.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        
        prods = Product.objects.filter(name__icontains=search_query)

    return render(request, 'webpage/search.html', {'prods': prods, 'form': form})
