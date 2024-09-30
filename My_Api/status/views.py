from .models import Status  # status/model
from .serializers import StatusSerializer  # Serializers based on status/model

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics

# Create your views here.


class StatusAPIView(APIView):
    def get(self, request, fromate=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list, many=True)

        return Response(status_serializer.data)


class StatusListApiView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusCreateApiView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetailsView(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"


class StatusUpdateView(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"


class StatusDeleteView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
