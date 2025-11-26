from django.urls import path
from Ayur_admin import views

urlpatterns=[
    path('Admin_Dashboard/',views.admin_dashboard,name="admin_dashboard"),
    path('Add_category/',views.add_category,name="add_category"),
    path('Save_Add_category/',views.save_add_category,name="save_add_category"),
    path('Display_category/',views.display_category,name="display_category"),
    path('Edit_category/<int:category_id>/',views.edit_category,name="edit_category"),
    path('Update_category/<int:c_id>/',views.update_category,name="update_category"),
    path('Delete_category/<int:category_id>/',views.delete_category,name="delete_category"),

    path('Add_Products/',views.add_products,name="add_products"),
]