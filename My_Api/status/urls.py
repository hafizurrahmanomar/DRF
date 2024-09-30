from django.urls import path

from .views import (StatusAPIView, StatusListApiView,
StatusCreateApiView, StatusDetailsView, StatusUpdateView, StatusDeleteView)

urlpatterns = [
    path('status/', StatusAPIView.as_view()),
    path('status/list/', StatusAPIView.as_view()),
    path('status/create/', StatusCreateApiView.as_view()),
    # path('status/detail/<pk>/', StatusDetailsView.as_view()),
    path('status/detail/<id>/', StatusDetailsView.as_view()),
    path('status/update/<id>/', StatusUpdateView.as_view()),
    path('status/delete/<id>/', StatusDeleteView.as_view()),
]
