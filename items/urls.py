from django.urls import path


from . import views

app_name = 'items'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.login_index, name='login_index'),
    path('items/search', views.search, name='search'),
    path('items/add', views.item_add, name='item_add'),
    path('items/modify/<int:item_id>/', views.item_modify, name='item_modify'),
    path('items/show_all', views.show_all, name='show_all'),
    path('items/show_type/<int:type_id>/', views.show_type, name='show_type'),
    path('items/show_status/<int:status_id>/', views.show_status, name='show_status'),
    path('items/show_detail/<int:item_id>/', views.show_detail, name='show_detail'),
    path('items/remove/<int:item_id>/', views.item_remove, name='item_remove'),
    path('items/delete/<int:item_id>/', views.item_delete, name='item_delete'),

]