from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from secureaccess.models import Element
from secureaccessapi.permissions import IsPasswordCorrect
from secureaccessapi.serializers import NewElementSerializer, GetElementSerializer


class CreateElementView(generics.CreateAPIView):
    serializer_class = NewElementSerializer
    permission_classes = (IsAuthenticated,)


class GetElementView(mixins.RetrieveModelMixin, GenericAPIView):
    serializer_class = GetElementSerializer
    permission_classes = (IsPasswordCorrect,)

    def get_object(self):
        element = Element.get_valid_obj(self.kwargs['uuid'])
        if element is None:
            raise Http404()
        self.check_object_permissions(self.request, element)
        element.update_accessed()
        return element

    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class Stats(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(Element.get_stats())
