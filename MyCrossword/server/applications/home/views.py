from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action

from . import models, serializers

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'uid'

    def validate_request(self, request):
        validator = self.get_serializer(data=request.data)
        validator.is_valid(raise_exception=True)
        return validator.data

    @action(detail=False, methods=['patch'])
    def mark_as_visited(self, request, pk=None):
        validated_data = self.validate_request(request)
        user, _ = User.objects.get_or_create(uid=validated_data['uid'])
        serializer = self.get_serializer(user, data={'visitNum': user.visitNum + 1}, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        # catch all exceptions
        except (Exception, ):
            return JsonResponse(data={}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
