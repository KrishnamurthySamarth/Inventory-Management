from django.contrib import admin
from django.urls import path,include
from IventoryManager import views
 
urlpatterns = [
    path("", views.Home, name='Home'),
    path("Home/", views.Home, name='Home'),
    path("Home/", views.contact_us, name='contact'),
    path("IventoryManager/signup",views.sign_up, name='signup'),
    path("IventoryManager/signin",views.sign_in, name='signin'),
    path("IventoryManager/manage_page",views.manage_page,name='manage_page'),
    path("add/",views.items_to_add, name='add'),
    path("adding/",views.items_to_add,name='adding'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path("IventoryManager/edit",views.edit_item,name='edit'),
     path('sign_in/', views.sign_in, name='sign_in'),
    path("del/",views.delete_item,name='del'),
]