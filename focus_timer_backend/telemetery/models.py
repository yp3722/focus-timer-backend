from django.db import models

class PerformanceMetrics(models.Model):
    load_time = models.FloatField()
    render_time = models.FloatField()
    bottleneck_description = models.TextField(blank=True)

class ErrorTracking(models.Model):
    js_error = models.TextField()
    frequency = models.IntegerField()
    stack_trace = models.TextField()

class UserInteraction(models.Model):
    user_action = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class NetworkRequest(models.Model):
    api_endpoint = models.URLField()
    response_time = models.FloatField()
    status_code = models.IntegerField()

class DeviceInfo(models.Model):
    device_type = models.CharField(max_length=1500)
    operating_system = models.CharField(max_length=500)
    browser_version = models.CharField(max_length=1500)
    timestamp = models.DateTimeField()
