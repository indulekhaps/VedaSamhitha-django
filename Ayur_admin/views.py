from django.shortcuts import render,redirect
from Ayur_admin.models import Categorydb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def admin_dashboard(request):
    return render(request,"Dashboard.html")

def add_category(request):
    return render(request,"Add_Category.html")

def save_add_category(request):
    if request.method == "POST":
        c_name=request.POST.get('name')
        c_desc=request.POST.get('description')
        c_img=request.FILES['image']
        obj=Categorydb(CategoryName=c_name,Description=c_desc,CategoryImage=c_img)
        obj.save()
        return redirect(add_category)

def display_category(request):
    data=Categorydb.objects.all()
    return render(request,"Display_Category.html",{'data':data})

def edit_category(request,category_id):
    Category=Categorydb.objects.get(id=category_id)
    return render(request,"Edit_Category.html",{'Category':Category})

def update_category(request,c_id):
    if request.method == "POST":
        c_name=request.POST.get('name')
        c_desc=request.POST.get('description')
        try:
            c_img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(c_img.name,c_img)
        except MultiValueDictKeyError:
            file=Categorydb.objects.get(id=c_id).CategoryImage
    Categorydb.objects.filter(id=c_id).update(CategoryName=c_name,Description=c_desc,CategoryImage=file)
    return redirect(display_category)

def delete_category(request,category_id):
    data=Categorydb.objects.filter(id=category_id)
    data.delete()
    return redirect(display_category)

def add_products(request):
    return render(request,"Add_Products.html")





