import datetime

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.cache import RedisShorUrlCache
from apps.models import ShortUrl
from apps.serializers import ShortUrlCreateRequestSerializer, ShortUrlInfoResponseSerializer


class ShortenUrlApiView(GenericViewSet):
    serializer_class = ShortUrlInfoResponseSerializer
    shorten_url_params = [
        openapi.Parameter('short_url', openapi.IN_QUERY, type=openapi.TYPE_STRING),
    ]

    @swagger_auto_schema(request_body=ShortUrlCreateRequestSerializer)
    @action(methods=['POST'], detail=False, url_path='make')
    def create_short_url(self, request):
        serializer = ShortUrlCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(ShortUrlInfoResponseSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(manual_parameters=shorten_url_params)
    @action(methods=['GET'], detail=False, url_path='info')
    def get_short_url(self, request):
        short_url = request.GET.get('short_url')

        origin_url = RedisShorUrlCache().get(short_url)
        if not origin_url:
            shorten_url = get_object_or_404(ShortUrl, short_url=short_url)
            if shorten_url.expired_at < datetime.datetime.now().astimezone():
                raise NotFound()

            origin_url = shorten_url.origin_url
            RedisShorUrlCache().set(key=short_url, value=origin_url)

        return Response({
            'origin_url': origin_url,
            'short_url': short_url,
        })
