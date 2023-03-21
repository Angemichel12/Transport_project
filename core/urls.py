from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers


router = routers.SimpleRouter()
router.register('transport', views.TransportViewset, basename='transport')


urlpatterns = [
    path('allBus',views.Bus_list),
    path('allBus/<int:id>',views.Bus_detail),
    path('categories_list/', views.categories_list),
    path('categories_details/<int:id>/', views.categories_details),
    path('login/', obtain_auth_token),
]+router.urls
urlpatterns = format_suffix_patterns(urlpatterns)
