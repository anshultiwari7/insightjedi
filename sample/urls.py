from rest_framework.routers import DefaultRouter
from sample.views import DocumentViewSet

router = DefaultRouter()
router.register(r'document', DocumentViewSet, basename='document')
urlpatterns = router.urls