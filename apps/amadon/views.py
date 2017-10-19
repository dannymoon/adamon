from django.shortcuts import render, HttpResponse, redirect

def index(request):
    
    return render(request, 'amadon/index.html')

def buy(request):
    if request.method == "POST":
        if 'quantity_ordered' not in request.session:
            request.session['quantity_ordered'] = 0
        if 'total_price' not in request.session:
            request.session['total_price'] = 0
        
        price = float(request.POST["quantity"]) * float(request.POST["price"])
        request.session['price'] = price
        request.session['quantity_ordered'] += int(request.POST["quantity"])
        request.session['total_price'] += price
    return redirect('/amadon/checkout')

def checkout(request):
    
    
    return render(request, 'amadon/result.html')
# Create your views here.
# from django.shortcuts import render, redirect

# # Create your views here.
# def index(request):
#     return render(request, 'shop/index.html')

# def process_buy(request):
#     if not 'quantity_ordered' in request.session:
#             request.session['quantity_ordered'] = 0
#     if not 'price_ordered' in request.session:
#             request.session['price_ordered'] = 0
#     if request.method == "POST":
#         if request.POST['product_id'] == 'item1':
#             price = 20
#         elif request.POST['product_id'] == 'item2':
#             price = 30
#         elif request.POST['product_id'] == 'item3':
#             price = 5
#         request.session['checkout_price'] = int(request.POST['quantity']) * price
#         request.session['quantity_ordered'] += int(request.POST['quantity'])
#         request.session['price_ordered'] += request.session['checkout_price']
#         # print '@@@price', request.session['checkout_price']
#     return redirect('/checkout')

# def checkout(request):
#     return render(request, 'shop/checkout.html')

# def back(request):
#     return redirect('/')