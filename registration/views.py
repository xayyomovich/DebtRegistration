from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm, Customer
from .models import Customer

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # You'll need to define this URL
    else:
        form = CustomerForm()
    return render(request, 'registration/customer_form.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'registration/customer_list.html', {'customers': customers})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'registration/customer_form.html', {'form': form})


