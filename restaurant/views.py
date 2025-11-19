from django.shortcuts import render,redirect,get_object_or_404
from .models import MenuItem,Order

# Create your views here.
def home(request):
    return render(request, 'restaurant/home.html')

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'items': items})

def order(request):
    if request.method == 'POST':
        name = request.POST['customer_name']
        selected_items = request.POST.getlist('items')
        total = 0
        order = Order(customer_name=name, total_amount=0)
        order.save()
        for item_id in selected_items:
            item = MenuItem.objects.get(id=item_id)
            order.items.add(item)
            total += item.price
        order.total_amount = total
        order.save()
        return redirect('bill', order_id=order.id)
    items = MenuItem.objects.all()
    return render(request, 'restaurant/order.html', {'items': items})

def bill(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'restaurant/bill.html', {'order': order})

