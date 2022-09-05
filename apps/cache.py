from django.core.cache import cache

from apps.constants import EXPIRE_SHORT_URL


class RedisShorUrlCache:
    """
        prefix-key = short_url
        value = origin_url
    """
    prefix_key = 'shorten_url'

    def set(self, key, value):
        cache.set('{}-{}'.format(self.prefix_key, key), value, timeout=EXPIRE_SHORT_URL.total_seconds())

    def get(self, key):
        return cache.get('{}-{}'.format(self.prefix_key, key))
