from authentication import views 
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'users', views.UserViewSet)


urlpatterns = router.urls