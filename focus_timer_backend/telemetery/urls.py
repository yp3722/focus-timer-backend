from django.urls import path
from .views import (PerformanceMetricsView, ErrorTrackingView, 
                    UserInteractionView, NetworkRequestView, DeviceInfoView)

urlpatterns = [
    path('performance-metrics/', PerformanceMetricsView.as_view(), name='performance_metrics'),
    path('error-tracking/', ErrorTrackingView.as_view(), name='error_tracking'),
    path('user-interactions/', UserInteractionView.as_view(), name='user_interactions'),
    path('network-requests/', NetworkRequestView.as_view(), name='network_requests'),
    path('device-info/', DeviceInfoView.as_view(), name='device_info'),
]
