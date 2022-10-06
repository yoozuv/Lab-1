from django.urls import path
from wishlist.views import show_wishlist,show_xml,show_json,show_json_by_id,show_xml_by_id,register,login_user,logout_user,ajax_function,ajax_form




app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('ajax/',ajax_function,name='ajax_function'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),  
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('submit/',ajax_form,name='ajax_form'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]