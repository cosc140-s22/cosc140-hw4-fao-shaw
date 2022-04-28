from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
  products = Product.objects.all().order_by('name')
  context = {'products': products}
  return render(request, 'products/index.html', context)

def show(request, product_id):
  view = get_object_or_404(Product, pk= product_id)
  context = { 'product':view }
  return render(request,'products/show.html', context)