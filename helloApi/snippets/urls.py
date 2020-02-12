from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UserList.as_view()), 
    path('users/<int:pk>/', views.UserDetail.as_view()),       
    path('list/', views.SnippetList.as_view()  , name ='snippet-list'),
    path('list/<int:pk>/', views.SnippetDetail.as_view(), name ='snippet-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
