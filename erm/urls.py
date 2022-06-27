from django import views
from django.urls import path
from .views import *

app_name = 'erm'

urlpatterns = [
     path('product_list/', ProductListView.as_view(), name='product-list'),
     path('product_create/', ProductCreateView.as_view(), name='product-create'),
     path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
     path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product-update'),
     path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product-delete'),
     path('cost_list/', CostListView.as_view(), name='cost-list'),
     path('cost_create/', CostCreateView.as_view(), name='cost-create'),
     path('cost_detail/<int:pk>', CostDetailView.as_view(), name='cost-detail'),
     path('cost_update/<int:pk>', CostUpdateView.as_view(), name='cost-update'),
     path('cost_delete/<int:pk>', CostDeleteView.as_view(), name='cost-delete'),
     path('note_list/', notelist, name='notelist'),
     path('note_list_rep/', notelistrep, name='notelist-rep'),
     # path('po/', POCreate, name='po-create'),
     #path('po_list/', POListView.as_view(), name='po-list'),
     #path('po_create/', poc, name='create-po'),
     #path('htmx/poitem-form/', create_poitem_form, name="poitem-form"),
     #path('htmx/poitem/<int:pk>/', detail_poitem, name="detail-poitem"),
     #path('htmx/poitem/<int:pk>/delete/', delete_poitem, name="delete-poitem"),
     #path('htmx/poitem/<int:pk>/update/', update_poitem, name="update-poitem"),
     #path('<int:pk>/', create_poitem, name="create-poitem"),
     path('doc_list/', DocListView.as_view(), name='doc-list'),
     path('doc_create/', doc_create, name='doc-create'),
     path('docitem-form/', create_docitem_form, name="docitem-form"),
     path('docitem/<int:pk>/', docitem_create, name="docitem-create"),
     path('docitem/<int:pk>/detail', detail_docitem, name="detail-docitem"),
     path('docitem/<int:pk>/list', docitem_list, name="list-docitem"),
     path('docitem/<int:pk>/delete/', delete_docitem, name="delete-docitem"),
     path('docitem/<int:pk>/update/', update_docitem, name="update-docitem"),
     
]