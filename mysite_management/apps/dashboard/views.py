from django.shortcuts import render
from apps.users.models import User
from apps.product.models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    users_obj = User.objects.all().order_by('-id')
    admin = User.objects.filter(user_role_id=1).count()
    staff = User.objects.filter(user_role_id=2).count()
    vendors = User.objects.filter(user_role_id=3).count()
    products = Product.objects.all().order_by('-id')

    totalRecord = users_obj.count()
    paginator = Paginator(users_obj, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'admin': admin,
        'merchants': staff,
        'vendors': vendors,
        'products':products,
        'users_obj':users_obj,
        'totalRecord': totalRecord,
    }
    return render(request, 'dashboard/index.html', context)

