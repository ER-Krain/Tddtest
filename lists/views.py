from django.http import HttpResponse
from django.shortcuts import redirect,render
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        #new_item_text = request.POST['item_text'] #1
        Item.objects.create(text=request.POST['item_text'])
        #Item.objects.create(text=new_item_text) #2
        return redirect('/')

    items = Item.objects.all()
    
    return render(request,'home.html', {'items':items})
