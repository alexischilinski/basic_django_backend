from rest_framework import routers
from .views import ReviewViewSet, RegisterView

router = routers.DefaultRouter()

router.register('reviews', ReviewViewSet, 'reviews')
router.register('register', RegisterView, 'register')

urlpatterns = router.urls