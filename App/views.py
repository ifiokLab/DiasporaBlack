from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from .forms import *
from django.contrib.auth import get_user_model, login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
# Create your views here.

def Home(request):
    product = Product.objects.all()
    return render(request,'App/home.html',{'product':product})

from django.contrib.auth.views import LoginView
from django.urls import is_valid_path, reverse_lazy

class customer_login(LoginView):
    template_name = 'App/customer-login.html'
    form_class = CustomerLoginForm
    next_page = 'home'
   




def customer_signup(request):
    if request.method == 'POST':
        print(request.POST)
        
        form = CustomerCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
           
            login(request, user)  # Log in the user
            return redirect('home')  # Redirect to the login page after successful signup
    else:
        form = CustomerCreationForm()
    
    return render(request, 'App/customer-signup.html', {'form': form})



def Logout(request):
    logout(request)
    return redirect('customer_login')  # Redirect to the homepage after logout

def product_detail(request,pk):
    
    product = Product.objects.get(id = pk)
    if SavedItem.objects.filter(user=request.user,product = product).exists():
        saved_item = SavedItem.objects.filter(user=request.user,product = product)
    else:
        saved_item = False
    num = (product.discount_price/product.price) * 100
    discount_rate = round(num,1)
    return render(request,'App/product-detail.html',{'product':product,'discount_rate': discount_rate,'saved_item':saved_item})

def product_cart(request):
    if CustomerAccount.objects.filter(user = request.user).exists():
        account = CustomerAccount.objects.get(user = request.user)
    else:
        account = False
    return render(request,'App/product-cart.html',{'account':account})




@login_required(login_url = 'customer_login')
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk )
    order_item,a = OrderProduct.objects.get_or_create(
        product = item,
        user = request.user,
        ordered = False
    )
    print(a)
    print(order_item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    #print(order_qs)
    #print(order_qs.exists())
    if order_qs.exists():#check if order exists
        #print(order_qs[0])
        order = order_qs[0]#grab user who made the order

        if order.product.filter(product__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("order-summary")
        else:
            order.product.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.product.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("order-summary")

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk )
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.product.filter(product__pk=item.pk).exists():
            order_item = OrderProduct.objects.filter(
                product=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.delete()
            messages.info(request, "Item \""+order_item.product.name+"\" remove from your cart")
            return redirect("order-summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("product", pk=pk)
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("product", pk = pk)


@login_required
def reduce_quantity_item(request, pk):
    item = get_object_or_404(Product, pk=pk )
    order_qs = Order.objects.filter(
        user = request.user, 
        ordered = False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.product.filter(product__pk=item.pk).exists() :
            order_item = OrderProduct.objects.filter(
                product = item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                #order_item.delete()
                order_item.quantity = 1
            messages.info(request, "Item quantity was updated")
            return redirect("order-summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("order-summary")
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("order-summary")




class OrderSummaryView(LoginRequiredMixin, View):
    login_url = 'customer_login'
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
           
            #num = (order.product.discount_price / order.product.price) *100
            #discount_rate = round(num,2)
            if CustomerAccount.objects.filter(user = self.request.user).exists():
                account = CustomerAccount.objects.get(user = self.request.user)
            else:
                account = False
            context = {
                'object': order,
                'account':account,
                #'discount_rate':discount_rate,
            }
            return render(self.request, 'App/product-cart.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("/")



@login_required(login_url='customer_login')
def customer_account(request):
    customer = myuser.objects.get(id = request.user.id)
    if CustomerAccount.objects.filter(user = request.user).exists():
        account = CustomerAccount.objects.get(user = request.user)
    else:
       
        account = False
    return render(request,'App/account-overview.html',{'customer':customer,'account':account})



@login_required(login_url='customer_login')
def create_customer_address(request):
    customer = myuser.objects.get(id = request.user.id)
    if CustomerAccount.objects.filter(user = request.user).exists():
        account = CustomerAccount.objects.get(user = request.user)
        form1 = CustomerAccountForm(instance = account)
    else:
        form1 = CustomerAccountForm()
        account = None
   
    if request.method == 'POST':
        form2 = EditUser(instance = customer,data=request.POST)
        form1 = CustomerAccountForm(instance = account,data=request.POST)
        print(form1.errors)
        if form2.is_valid() and form1.is_valid():
            form2.save()
            form1.save()
            return redirect('customer-account')
    else:
        form2 = EditUser(instance = customer)
   
    return render(request,'App/address-book.html',{'form1':form1,'form2': form2,'account': account})






class CheckoutView(LoginRequiredMixin,View):
    login_url = '/customer-login/'
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        order = Order.objects.get(user=self.request.user, ordered=False)
        account = CustomerAccount.objects.get(user = self.request.user)
        context = {
            'form': form,
            'order': order,
            'account':account,
        }
      
        return render(self.request, 'App/check-out.html', context)
    
    def post(self,*args,**kwargs):
        print(self.request.POST)
        form = CheckoutForm(self.request.POST or None)
  
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                payment_option = form.cleaned_data.get('payment_option')
                order.save()
                if payment_option == 'P':
                    return redirect('payment')
            return redirect('payment')   
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("order-summary")
        #return redirect('home')



class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        amount = int(order.get_total_price() * 100)  #cents
        context = {
            'order': order,
            'amount':amount,
        }
        return render(self.request, "App/payment.html", context)

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        payment = Payment()
        payment.user = self.request.user
        payment.amount = order.get_total_price()
        payment.save()
      
        # assign payment to order
        print('before',order.ordered)
        order.ordered = True
        order.payment = payment
        print('After',order.ordered)
        order.save()

        return redirect('home')
        

       
#checkout address
class CheckoutAddress(LoginRequiredMixin,View):
    login_url = '/customer-login/'
    def get(self, *args, **kwargs):
        form1 = CustomerAccountForm()
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {
            'form1': form1,
            'order': order
        }
      
        return render(self.request, 'App/checkout-address.html', context)
    
    def post(self,*args,**kwargs):
        print(self.request.POST)
        form1 = CustomerAccountForm(self.request.POST or None)
  
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form1.is_valid():
                form1.save()
                return redirect('checkout')
            else:
                # Handle the case when the form is not valid
                order = Order.objects.get(user=self.request.user, ordered=False)
                context = {
                    'form1': form1,
                    'order': order
                }
                return render(self.request, 'App/checkout-address.html', context)
                
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("order-summary")
        #return redirect('home')

def save_product(request, productId):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=productId)
        if SavedItem.objects.filter(user=request.user, product=product).exists():
            messages.error(request, 'Product already added to saved items!')
        else:
            SavedItem.objects.create(user=request.user, product=product)
            messages.success(request, 'Product has been saved!')
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=500)



def remove_save_product(request, productId):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=productId)
        SavedItem.objects.get(user=request.user, product=product).delete()
        messages.success(request, 'Product has been removed!')
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=500)


def SaveLater(request):
    if SavedItem.objects.filter(user=request.user).exists():
        data = SavedItem.objects.filter(user=request.user)
        return render(request,'App/saved-items.html',{'data':data})
    else:
        return render(request,'App/empty-saved-items.html')





#seller

class seller_login(LoginView):
    template_name = 'App/seller-login.html'
    form_class = SellerLoginForm
    next_page = 'seller-dashboard'
   



def seller_signup(request):
    if request.method == 'POST':
        print(request.POST)
        
        form = SellerCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
           
            login(request, user)  # Log in the user
            return redirect('home')  # Redirect to the login page after successful signup
    else:
        form = SellerCreationForm()
    
    return render(request, 'App/seller-signup.html', {'form': form})


def seller_dashboard(request):
    return render(request,'App/seller-dashboard.html')


def seller_orders(request):
    return render(request,'App/seller-orders.html')


def seller_customer(request):
    return render(request,'App/seller-customer.html')



def seller_settings(request):
    if Seller.objects.filter(user = request.user).exists():
        seller = Seller.objects.get(user  = request.user)
    else:
        seller = None
    if request.method == 'POST':
       
        form =  SellerForm(data = request.POST,files = request.FILES,instance = seller)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('seller-dashboard')
    else:
        form =  SellerForm(instance = seller)
    return render(request,'App/seller-settings.html',{'form':form,})



def create_product(request):
    if Seller.objects.filter(user = request.user).exists():
        seller = Seller.objects.get(user  = request.user)
    else:
        seller = None
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seller-dashboard')
    else:
        form = ProductForm()
    return render(request,'App/create-product.html',{'form':form,'seller':seller})

def product_list(request):
    product = Product.objects.filter(seller__user = request.user)
    return render(request,'App/product-list.html',{'product': product})


def edit_product(request,pk):
    product = Product.objects.get(id = pk,seller__user = request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller-dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request,'App/edit-product.html',{'form': form})












