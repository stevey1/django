from django.urls import path,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'list', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    #path('', views.api_root),
    path('',include(router.urls))
]
#urlpatterns = format_suffix_patterns(urlpatterns)
'''
    path('list/',
        views.SnippetList.as_view(), name='snippet-list'), path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(), name='snippet-detail'),
    path('list/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),  name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(), name='user-detail')
'''

