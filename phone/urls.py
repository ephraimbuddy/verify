from phone import views 
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'phones', views.PhoneViewset)

urlpatterns = [
    path('send_sms_code/',views.send_sms_code),
    path('verify_phone/<int:sms_code>',views.verify_phone),
]

urlpatterns += router.urls