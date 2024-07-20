from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from social_django.utils import psa
from rest_framework.authtoken.models import Token
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@psa('social:complete')
def exchange_token(request, backend):
    # logger.info("Req: %s", request)
    # logger.info("Exchange token called with backend: %s", backend)
    user = request.backend.do_auth(request.data.get('access_token'))
    logger.info("user: %s", user)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Authentication failed'}, status=400)
