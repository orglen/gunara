from django.urls import path
from backend.api import views

urlpatterns = [ 
    path('conversation',views.conversation ),
    path('conversation/<uuid:conversation_id>', views.conversation,name='conversation_id'),
    path('get_title/<uuid:conversation_id>', views.get_title,name='get_title'),
    path('get_conversations', views.get_conversations,name='get_conversations'),
    path('del_title', views.del_title,name='del_title'),
] 