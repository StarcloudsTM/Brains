# views.py
from django.core.paginator import Paginator

def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 5)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'products.html', {'products': products})
