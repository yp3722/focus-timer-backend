from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from .models import PerformanceMetrics, ErrorTracking, UserInteraction, NetworkRequest, DeviceInfo
from .serializers import (PerformanceMetricsSerializer, ErrorTrackingSerializer, 
                          UserInteractionSerializer, NetworkRequestSerializer, DeviceInfoSerializer)

logger = logging.getLogger(__name__)

class PerformanceMetricsView(APIView):
    def post(self, request):
        serializer = PerformanceMetricsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ErrorTrackingView(APIView):
    def post(self, request):
        serializer = ErrorTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserInteractionView(APIView):
    def post(self, request):
        serializer = UserInteractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NetworkRequestView(APIView):
    def post(self, request):
        serializer = NetworkRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceInfoView(APIView):
    def post(self, request):
        serializer = DeviceInfoSerializer(data=request.data)
        logger.info(request.data);
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
