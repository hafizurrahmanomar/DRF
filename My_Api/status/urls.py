from django.urls import path


# part-01

# from .views import (StatusListApiView,StatusAPIView,StatusCreateApiView,StatusUpdateView,StatusDeleteView)

# Part-02
#from .views import (StatusListCreateApiView,StatusDetailsView)

# Part-03
# from .views import (StatusListCreateAPIView,StatusRetrieveUpdateDestroyAPIView)

# Part-04
from .views import StatusViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
    
#     # Part-03

#     # path('status/', StatusListCreateAPIView.as_view()),
#     # path('status/<id>/', StatusRetrieveUpdateDestroyAPIView.as_view()),
    
    
#     # Part-02
#     # path('status/', StatusListCreateApiView.as_view()),
#     # path('status/<id>/', StatusDetailsView.as_view()),
    
#     #part-01
#     #path('status/detail/<id>/', StatusDetailsView.as_view()),
#     # path('status/list/', StatusListApiView.as_view()),
#     # path('status/', StatusAPIView.as_view()),
#     # path('status/create/', StatusCreateApiView.as_view()),
#     # path('status/update/<id>/', StatusUpdateView.as_view()),
#     # path('status/delete/<id>/', StatusDeleteView.as_view()),

# ]


#Part -04

router = DefaultRouter()
router.register(r'status',StatusViewSet,basename='status')

urlpatterns = []+router.urls
