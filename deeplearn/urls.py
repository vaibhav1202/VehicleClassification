from django.urls import path
from .views import *
from rest_framework import routers
from deeplearn import views
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter() 
router.register(r'deep', views.deepViewSet)

urlpatterns = [
    path('create/', deepUploadView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),        
]