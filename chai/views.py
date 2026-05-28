from django.shortcuts import render
from .forms import ChaiVarityForm
from .models import Store

# Create your views here.
def all_chai(req):
    return render(req, 'chai/all_chai.html')

def chai_store_view(req):
    stores = None
    if req.method == 'POST':
        form = ChaiVarityForm(req.POST)
        
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_varity)
    else:
        form = ChaiVarityForm()

    return render(req, 'chai/chai_stores.html', {'form': form, 'stores': stores})