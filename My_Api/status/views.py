from .models import Status  # status/model
from .serializers import StatusSerializer  # Serializers based on status/model

# from rest_framework.views import APIView
# from rest_framework.response import Response

#from rest_framework import generics, mixins

from rest_framework import generics,parsers

# Create your views here.


# class StatusListCreateApiView(generics.ListAPIView, mixins.CreateModelMixin):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


# class StatusDetailsView(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"
#     # Total prameter update

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     # Only targated value update
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)

#    # self=super=main class
#     def delete(self, request, *args, **kwargs):
#         return super().delete(request, *args, **kwargs)

# class StatusListApiView(generics.ListAPIView, mixins.CreateModelMixin):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusAPIView(APIView):
#     def get(self, request, fromate=None):
#         status_list = Status.objects.all()
#         status_serializer = StatusSerializer(status_list, many=True)

#         return Response(status_serializer.data)


# class StatusCreateApiView(generics.CreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


# class StatusUpdateView(generics.UpdateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"


# class StatusDeleteView(generics.DestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"

# GET, POST
class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes =[parsers.FormParser,parsers.MultiPartParser]


# GET, PUT, PATCH, DELETE,
class StatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
