from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('allBus',views.Bus_list),
    path('allBus/<int:id>',views.Bus_detail)
]
urlpatterns = format_suffix_patterns(urlpatterns)
