from rest_framework import routers

from apps.views import ShortenUrlApiView

router = routers.DefaultRouter()
router.register('shorten', ShortenUrlApiView, basename='shorten')
urlpatterns = router.urls
