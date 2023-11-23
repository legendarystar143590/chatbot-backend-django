from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import commentViewSet, postViewSet

app_name = "posts"

router = DefaultRouter()
router.register(r"^(?P<post_id>\d+)/comment", commentViewSet)
router.register(r"", postViewSet)


urlpatterns = [
    path("", include(router.urls)),
   
]
