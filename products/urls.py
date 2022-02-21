from django.urls import path,include
from products import views

urlpatterns = [

    path('form',views.product_form),
    path('cart/<int:p_id>',views.cart,name='cart'),
    path('details',views.details, name='details'),
    path('cartdetails',views.details, name='details'),
    path('contactdetails/',views.contactdetails, name='contactdetails'),
    path('deleteuser/<int:p_id>',views.deleteuser, name='deleteuser'),
    path('updateuser/<int:p_id>',views.updateuser, name='updateuser'),
    path('edituser/<int:p_id>',views.editdetails,name="edituser"),
    path('view/',views.view, name='view'),
    path('addproduct/',views.addproduct, name='addproduct'),
    path('view/',views.view, name='view'),
  




]