from django.urls import path
from NiceApp import views


urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('editcategory/<int:dataid>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('', views.loginpage, name="loginpage"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecontact/<int:dataid>/', views.deletecontact, name="deletecontact"),
    path('addnewspage/', views.addnewspage, name="addnewspage"),
    path('savenews/', views.savenews, name="savenews"),
    path('displaynews/', views.displaynews, name="displaynews"),
    path('deletenews/<int:dataid>/', views.deletenews, name="deletenews"),

]