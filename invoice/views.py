from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import User, Product, Organisation, Order, OrderProduct, PdfUplaod

from . import api
import os

def create_new_user(user_name):
    
    newUser = User.objects.create(name = user_name) 
    newUser.save()
    
    return newUser
    

def add_new_product(item):
    
    name = item['description']
    date = item['date']
    price = item['price']
    quantity = item['quantity']
    tax =  item['tax']
    total = item['discount']
    
    newProduct = Product.objects.create(name= name, time= date, price= price, quantity= quantity, total = total) 
    newProduct.save()
    return newProduct

def add_new_organisation(org_name):
    
    newOrg = Organisation.objects.create(name= org_name ) 
    newOrg.save()
    return newOrg


def create_new_order(user, biller, vender, time, file):
    
    newOrder = Order.objects.create(user= user, to_org= biller, from_org= vender, time= time, pdf= file)
    newOrder.save()
    return newOrder
    
def upload_pdf(file):
    
    newPDF = PdfUplaod.objects.create(pdf= file)
    newPDF.save()
    return newPDF  

def upload(request):
    
    if(request.method=='POST'):
        
        user_name =request.POST['username']
            
        pdf_file = request.FILES["file"]
        
        pdf_obj = upload_pdf(pdf_file)
        pdf = pdf_obj.pdf
        
        # Create new user with help of name.
        user = create_new_user(user_name)
        
        data =  api.InvoiceAPI(pdf)
        # print(data)
        
        to_org = data['bill_to_name']
        from_org = data['vendor']['name']
        
        biller = add_new_organisation(to_org)
        vender = add_new_organisation(from_org)
        
        new_order = create_new_order(user, biller, vender, data['date'], pdf_obj)
        
        
        
        # List of all products, 
        for item in data['line_items']:
            
            # Mapping in between product and order.
            new_product = add_new_product(item)
            
            mapping_between_product_order = OrderProduct(order = new_order, product = new_product)
            mapping_between_product_order.save()
    
    
        

    return render(request,'upload.html')


'''

   Return the order which is related to given organisations('org_name').
   1. If recievcer is 'org_name'.
   2. If sender is 'ord_name'.
   
'''

def search_biller(org_name):
    
    order_list = Order.objects.filter(to_org__name__contains = org_name)
    
    print(order_list)
    return order_list
    
    
def search_vender(org_name):
    
    
    order_list = Order.objects.filter(from_org__name__contains = org_name)
    
    print(order_list)
    return order_list
    
    
    
    
def search_product(name):
    
    
    
    products = OrderProduct.objects.filter(product__name__contains = name)
    
    # print(products)
    
    
    order_list = set()
    
    for product in products:
         order = product.order
         order_list.add(order)
    
    # print(order_list)
    return order_list


def base_url(base):
    
    
    url = 'media/'+str(base)
    return url

def search(request):
    
    if(request.method=='POST'):
        choice = request.POST['choice']
        query = request.POST['query']
        
        # print(choice)
        # print(query)
        if(choice== "biller"):
            results = search_biller(query)
        
        elif(choice == "vender"):
            results = search_vender(query)
        
        elif(choice == "product"):
            results = search_product(query)
        
        print(results)
        
        
        res_arr=[]
        
        for result in results:
            
            entry = {}
            entry['user'] = result.user.name
            entry['from'] = result.from_org.name
            entry['to'] = result.to_org.name
            entry['timestamp'] = result.time
            entry['pdf'] = base_url(result.pdf.pdf)
            
            res_arr.append(entry)
        
        print(res_arr)
        
        
        return render(request, 'result.html', {'results':res_arr})
            
    
    

    return render(request,'search.html')

def result(request):
    
    return render(request,'result.html')