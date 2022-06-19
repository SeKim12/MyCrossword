from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from .models import ButtonCount
from .serializers import ButtonCountSerializer
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@api_view(['PATCH'])
def press_button(request, pk):
    button_count, _ = ButtonCount.objects.get_or_create(
        pk=pk, defaults={'name': pk, 'frequency': 0})
    serializer = ButtonCountSerializer(
        button_count,
        data={
            'frequency': button_count.frequency + 1,
            'pressed': True},
        partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_frequency(request, pk):
    try:
        bc = ButtonCount.objects.get(pk=pk)
        return JsonResponse(
            data={
                'frequency': bc.frequency},
            status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return JsonResponse(
            data={
                'error': 'button count data for id {} does not exist'.format(pk)},
            status=status.HTTP_404_NOT_FOUND)
