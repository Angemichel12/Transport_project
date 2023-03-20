from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('allBus',views.Bus_list),
    path('allBus/<int:id>',views.Bus_detail),
    path('categories_list/', views.categories_list),
    path('categories_details/<int:id>', views.categories_details),
]
urlpatterns = format_suffix_patterns(urlpatterns)
