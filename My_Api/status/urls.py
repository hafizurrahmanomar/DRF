from django.urls import path

# from .views import (StatusListApiView,StatusAPIView,StatusCreateApiView,StatusUpdateView,StatusDeleteView)

#from .views import (StatusListCreateApiView,StatusDetailsView)
from .views import (StatusListCreateAPIView,StatusRetrieveUpdateDestroyAPIView)

urlpatterns = [

    path('status/', StatusListCreateAPIView.as_view()),
    path('status/<id>/', StatusRetrieveUpdateDestroyAPIView.as_view()),
    
    # path('status/', StatusListCreateApiView.as_view()),
    # path('status/<id>/', StatusDetailsView.as_view()),
    #path('status/detail/<id>/', StatusDetailsView.as_view()),
    # path('status/list/', StatusListApiView.as_view()),
    # path('status/', StatusAPIView.as_view()),
    # path('status/create/', StatusCreateApiView.as_view()),
    # path('status/update/<id>/', StatusUpdateView.as_view()),
    # path('status/delete/<id>/', StatusDeleteView.as_view()),

]
