from django.shortcuts import render,redirect
from NiceApp.models import Categorydb,Productdb, NewsDb
from WebApp.models import Contactdb,Userdb,CartDb,CheckoutDb
from django.contrib import messages

# Create your views here.
def homepage(request):
    data = Categorydb.objects.all()
    pro = NewsDb.objects.all()
    cat = Categorydb.objects.all()
    return render(request, "home.html",{'data':data, 'pro':pro, 'cat':cat})

def aboutpage(request):
    cat = Categorydb.objects.all()
    return render(request, "about.html",{'cat':cat})

def newspage(request):
    pro = NewsDb.objects.all()
    cat = Categorydb.objects.all()
    return render(request, "news.html",{'pro':pro, 'cat':cat})

def contactpage(request):
    data = Categorydb.objects.all()
    cat = Categorydb.objects.all()
    return render(request, "contact.html", {'data':data, 'cat':cat})

def savecontact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        sb = request.POST.get('subject')
        mg = request.POST.get('message')
        obj = Contactdb(Name=na, Email=em, Phone=ph, Subject=sb, Message=mg)
        obj.save()
        return redirect(contactpage)

def shoppage(request):
    data = Productdb.objects.all()
    cat = Categorydb.objects.all()
    return render(request, "shop.html",{'data':data, 'cat':cat})

def productpage(request, cat_name):
    pro = Productdb.objects.filter(Category=cat_name)
    cat = Categorydb.objects.all()
    return render(request, "product.html", {'pro':pro, 'cat':cat})

def singleproduct(request,dataid):
    pros = Productdb.objects.get(id=dataid)
    pro = Productdb.objects.all()
    cat = Categorydb.objects.all()
    return render(request, "singleproduct.html", {'pros':pros,'pro':pro, 'cat':cat})

def registerpage(request):
    data = Categorydb.objects.all()
    cat = Categorydb.objects.all()
    return render(request, "register.html",{'data':data, 'cat':cat})

def saveuser(request):
    if request.method == "POST":
        na = request.POST.get('uname')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        im = request.FILES['image']
        pwd = request.POST.get('password')
        obj = Userdb(User_Name=na, EmailId=em, Phone=ph, Image=im, Password=pwd)
        obj.save()
        messages.success(request, "Register Successfully...")
        return redirect(registerpage)

def userlogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if Userdb.objects.filter(User_Name=uname, Password=pwd).exists():
            request.session['User_Name'] = uname
            request.session['Password'] = pwd
            messages.success(request, "Login Successfully...")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid username or password...")
            return redirect(registerpage)
    else:
        messages.error(request, "Invalid username or password...")
        return redirect(registerpage)

def userlogout(request):
    del request.session['User_Name']
    del request.session['Password']
    messages.success(request, "Logout Successfully...")
    return redirect(registerpage)

# def singlenews(request,dataid):
#     data = NewsDb.objects.get(id=dataid)
#     cat = Categorydb.objects.all()
#     return render(request,"singlenews.html", {'data':data, 'cat':cat})

def cartpage(request):
    data = CartDb.objects.filter(User_Name=request.session['User_Name'])
    cat = Categorydb.objects.all()
    return render(request, "cart.html", {'data':data, 'cat':cat})


def savecart(request):
    if request.method == "POST":
        una = request.POST.get('uname')
        pna = request.POST.get('pname')
        br = request.POST.get('brand')
        qty = request.POST.get('qty')
        pr = request.POST.get('totalprice')
        obj = CartDb(User_Name=una, ProductName=pna, Brand=br, Quantity=qty, TotalPrice=pr)
        obj.save()
        return redirect(homepage)


def CartDelete(request, dataid):
    data = CartDb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpage)

def checkoutpage(request):
    return render(request, "checkout.html")

def savecheckout(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ad = request.POST.get('address')
        ph = request.POST.get('phone')
        mg = request.POST.get('message')
        obj = CheckoutDb(Name=na, Email=em, Address=ad, Phone=ph, Message=mg)
        obj.save()
        messages.success(request, "Order Successfully...")
        return redirect(homepage)