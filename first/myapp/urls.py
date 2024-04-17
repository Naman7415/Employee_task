from django.urls import path,include
from .views import*
from rest_framework import routers



router = routers.DefaultRouter() 
router.register(r'us', EmployeeView)

# Static URL pattern for UserListView
urlpatterns = [
    path('', include(router.urls)),
    path("apisearch/", UserListView.as_view()),
    # path("myapi/", MyView.as_view()),
    
]

