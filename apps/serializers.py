from rest_framework import serializers

from apps.cache import RedisShorUrlCache
from apps.key_gen_service import GenShortUrl
from apps.models import ShortUrl


class ShortUrlCreateRequestSerializer(serializers.Serializer):
    origin_url = serializers.CharField(max_length=511)

    def create(self, validated_data):
        short_url = GenShortUrl().generate()
        instance = ShortUrl.objects.create(origin_url=validated_data.get('origin_url'), short_url=short_url)
        RedisShorUrlCache().set(key=instance.short_url, value=instance.origin_url)
        return instance


class ShortUrlInfoRequestSerializer(serializers.Serializer):
    short_url = serializers.CharField()


class ShortUrlInfoResponseSerializer(serializers.Serializer):
    origin_url = serializers.CharField()
    short_url = serializers.CharField()
