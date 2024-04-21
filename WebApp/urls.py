from django.urls import path
from WebApp import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('newspage/', views.newspage, name="newspage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('shoppage/', views.shoppage, name="shoppage"),
    path('productpage/<cat_name>/', views.productpage, name="productpage"),
    path('singleproduct/<int:dataid>/', views.singleproduct, name="singleproduct"),
    path('', views.userlogin, name="userlogin"),
    path('registerpage/', views.registerpage, name="registerpage"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('userlogout/', views.userlogout, name="userlogout"),
    # path('singlenews/<int:dataid>/', views.singlenews, name="singlenews"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('savecart/', views.savecart, name="savecart"),
    path('CartDelete/<int:dataid>/', views.CartDelete, name="CartDelete"),
    path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
    path('savecheckout/', views.savecheckout, name="savecheckout"),

]