from rest_framework import routers
from .views import DefectViewset, ABCViewset, Price_min_maxViewset


router = routers.DefaultRouter()
router.register('api/defect', DefectViewset, 'defect')
router.register('api/abc', ABCViewset, 'ABC')
router.register('api/price', Price_min_maxViewset, 'price')

urlpatterns = router.urls