from django.shortcuts import render,redirect
from NiceApp.models import Categorydb,Productdb,NewsDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import Contactdb
from django.contrib import messages

# Create your views here.
def indexpage(request):
    return render(request, "index.html")

def addcategory(request):
    return render(request,"addcategory.html")

def savecategory(request):
    if request.method == "POST":
        cna = request.POST.get('cname')
        img = request.FILES['image']
        obj = Categorydb(CategoryName=cna, CategoryImage=img)
        obj.save()
        messages.success(request, "category Saved Successfully...")
        return redirect(addcategory)

def displaycategory(request):
    data = Categorydb.objects.all()
    return render(request, "displaycategory.html", {'data':data})

def editcategory(request, dataid):
    data = Categorydb.objects.get(id=dataid)
    messages.success(request, "Category Edit...")
    return render(request, "editcategory.html",{'data':data})

def updatecategory(request, dataid):
    if request.method == "POST":
        cna = request.POST.get('cname')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Categorydb.objects.get(id=dataid).CategoryImage
        Categorydb.objects.filter(id=dataid).update(CategoryName=cna, CategoryImage=file)
        messages.success(request, "Category Edited Successfully...")
        return redirect(displaycategory)

def deletecategory(request, dataid):
    data = Categorydb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Category delete...")
    return redirect(displaycategory)

def addproduct(request):
    data = Categorydb.objects.all()
    return render(request, "addproduct.html",{'data':data})

def saveproduct(request):
    if request.method == "POST":
        ct = request.POST.get('category')
        pn = request.POST.get('pname')
        pr = request.POST.get('price')
        br = request.POST.get('brand')
        ing = request.POST.get('ingredients')
        img = request.FILES['image']
        obj = Productdb(Category=ct, ProductName=pn, Price=pr, Brand=br, Ingredients=ing, Image=img)
        obj.save()
        messages.success(request, "Product Saved Successfully...")
        return redirect(addproduct)

def displayproduct(request):
    data = Productdb.objects.all()
    return render(request, "displayproduct.html",{'data':data})

def editproduct(request, dataid):
    data1 = Categorydb.objects.all()
    data = Productdb.objects.get(id=dataid)
    messages.success(request, "Product Edit...")
    return render(request, "editproduct.html",{'data1':data1, 'data':data})

def updateproduct(request, dataid):
    if request.method == "POST":
        ct = request.POST.get('category')
        pn = request.POST.get('pname')
        pr = request.POST.get('price')
        br = request.POST.get('brand')
        ing = request.POST.get('ingredients')
        try:
            ing = img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=dataid).Image
        Productdb.objects.filter(id=dataid).update(Category=ct, ProductName=pn, Price=pr, Brand=br, Ingredients=ing, Image=file)
        messages.success(request, "Product Edited Successfully...")
        return redirect(displayproduct)


def deleteproduct(request, dataid):
    data = Productdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Product delete...")
    return redirect(displayproduct)

def loginpage(request):
    return render(request, "login.html")

def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pwd
                messages.success(request, "Login Successfully...")
                return redirect(indexpage)
            else:
                messages.error(request, "Invalide username or password...")
                return redirect(loginpage)
        else:
            messages.error(request, "Invalide username or password...")
            return redirect(loginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...")
    return redirect(loginpage)

def displaycontact(request):
    data = Contactdb.objects.all()
    return render(request, "displaycontact.html", {'data':data})

def deletecontact(request, dataid):
    data = Contactdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Contact deleted...")
    return redirect(displaycontact)

def addnewspage(request):
    return render(request,"addnews.html")

def savenews(request):
    if request.method == "POST":
        na = request.POST.get('name')
        msg = request.POST.get('message')
        img = request.FILES['image']
        obj = NewsDb(Name=na, Message=msg, Image=img)
        obj.save()
        messages.success(request, "News Saved Successfully...")
        return redirect(addnewspage)

def displaynews(request):
    data = NewsDb.objects.all()
    return render(request,"displaynews.html", {'data':data})

def deletenews(request,dataid):
    data = NewsDb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "News Deleted...")
    return redirect(displaynews)

