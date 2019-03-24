from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST['prod_id'])
    total_charge = quantity_from_form * product.price
    print(f"Charging credit card... {total_charge}")
    order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session['order_id'] = order.id
    return redirect("/order")

def checkout_screen(request):
    order = Order.objects.get(id=request.session['order_id'])
    orders = Order.objects.all()
    total_spent = sum(ord.total_price for ord in orders)
    print(total_spent, '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    total_ordered = sum(ord.quantity_ordered for ord in orders)
    context = {
        'order': order,
        'total_spent': total_spent,
        'total_ordered': total_ordered,
    }
    return render(request, "store/checkout.html", context)
