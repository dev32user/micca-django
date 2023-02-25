from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request,'shop/list.html',{'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.product_detail = product.product_detail.replace("'", "").replace("[", "").replace("]", "")
            product.save()
            return redirect('shop:list')
    else:
        form = ProductForm()
    context = {'form':form}
    return render(request, 'shop/create.html', context)


def product_detail(request,pk):
    detail = Product.objects.get(pk=pk)
    return render(request, 'shop/detail.html', {'detail':detail})


def product_edit(request,pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        product.content = request.POST['content']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.product_detail = request.POST['product_detail']
        product.imgfile = request.FILES['imgfile']

        product.save()
        return redirect('shop:list')

    else:
        form = ProductForm
        return render(request, 'shop/edit.html', {'form':form})


def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('shop:list')

