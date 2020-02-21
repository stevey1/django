from django.urls import include, path
from rest_framework import routers
from snippets.views import UserViewSet, GroupViewSet, SnippetViewSet, CustomAuthToken
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'snippets', SnippetViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += [
    path('api-token-auth/', CustomAuthToken.as_view())
]