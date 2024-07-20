from rest_framework import serializers
from .models import PerformanceMetrics, ErrorTracking, UserInteraction, NetworkRequest, DeviceInfo

class PerformanceMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceMetrics
        fields = '__all__'

class ErrorTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorTracking
        fields = '__all__'

class UserInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInteraction
        fields = '__all__'

class NetworkRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkRequest
        fields = '__all__'

class DeviceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = '__all__'
