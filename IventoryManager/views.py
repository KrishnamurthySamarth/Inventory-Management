from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import Login_form,Signin_form,EditForm
from .models import Inventory_items
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import logout


# Create your views here.
def Home(request):
    return render(request , 'Home.html')

def contact_us(request):
    return render(request,'contact.html')

def sign_up(request):
    valid = False
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            valid = True
            user = form.save()
            return redirect('sign_in')
    else:
        form = Login_form()
    return render(request, 'login.html', {'form':form,'valid':valid})

def sign_in(request):
    valid = False
    if request.method=="POST":
        form = Signin_form(request, data = request.POST)
        if form.is_valid():
            print("yes")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print("YES")
            user = authenticate(request,username=username, password=password)
            if user is not None:
                valid = True
                login(request, user)
                return HttpResponseRedirect('manage_page')
        else:
            message = "user does not exist"
            print(message)
            return render(request,'sign_in.html',{'message':message,'form':form})
    else:
        form = Signin_form()
    return render(request, 'sign_in.html', {'form':form,'valid':valid})

def manage_page (request):
    is_empty = False
    user = request.user
    inventory_items = Inventory_items.objects.filter(user=user)
    if inventory_items.exists() == False:
        is_empty = True
    return render(request, 'managepage.html', {'inventory_items': inventory_items, 'is_empty': is_empty})
    
@login_required
def items_to_add(request):
    
    if request.method == "POST":
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        unit_price = request.POST.get('unit_price')
        dispatched_from = request.POST.get('dispatched_from')
        dispatched_price = request.POST.get('dispatched_price')

        if not item_name or not quantity or not unit_price:
            message = "Please fill the deatils in every feild avaialble"
            return render(request,'add_item.html',{'message':message})

        try:
            unit_price=float(unit_price)
            quantity=int(quantity)
            dispatched_price=float(dispatched_price)
        except:
            error = "Ivalid data type"
            return render(request,'add_item.html',{'message':error})    

        added = Inventory_items(item_name=item_name,quantity=quantity,Unit_price=unit_price,dispatched_from=dispatched_from,dispatched_price=dispatched_price, user=request.user)
        added.save()
    
        return HttpResponseRedirect(reverse('manage_page'))

    else:
        return render(request, 'add_item.html')

def edit_item(request):
    if request.method == 'POST':
        req_item = request.POST.get('item_name')
        items = Inventory_items.objects.filter(item_name=req_item, user=request.user)

        if items.exists():
            item_to_edit = items.first()  
            form = EditForm(request.POST, instance=item_to_edit)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('manage_page'))
    else:
        req_item = request.GET.get('item_name')  
        items = Inventory_items.objects.filter(item_name=req_item, user=request.user)

        if items.exists():
            item_to_edit = items.first() 
            form = EditForm(instance=item_to_edit)

    return render(request, 'edit_item.html', {'form': form})

def delete_item(request):
    if request.method == 'POST':
        req_item = request.POST.get('item_name')
        items = Inventory_items.objects.get(item_name=req_item, user=request.user)
        items.delete()
        return HttpResponseRedirect(reverse('manage_page'))


def custom_logout(request):
    logout(request)
    return redirect('Home')

        
