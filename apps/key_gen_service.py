from time import time

from django.utils.baseconv import base62

from apps.constants import INSTANCE_GEN_ID, EPOCH_TIME


class KGenerator:
    """
        time (ms)
        instance(int): 5 bit
        seq(int): 4 bit
    """
    MAX_SEQ = 2 ** 4 - 1

    def __init__(self, epoch: int = 0, instance: int = 1):
        current = int(time() * 1000)
        self._epo = epoch
        self._ts = current - self._epo
        self._inf = instance
        self._seq = 0

    def __next__(self):
        current = int(time() * 1000) - self._epo
        if self._ts == current:
            if self._seq == self.MAX_SEQ:
                return None
            self._seq += 1
        else:
            self._seq = 0

        self._ts = current
        return self._ts << 9 | self._inf << 4 | self._seq


class UuidGenerator:
    """
        time (ms)
        instance(int): 13 bit
        seq(int): 10 bit
    """
    MAX_SEQ = 2 ** 10 - 1

    def __init__(self, epoch: int = 0, instance: int = 1):
        current = int(time() * 1000)
        self._epo = epoch
        self._ts = current - self._epo
        self._inf = instance
        self._seq = 0

    def __next__(self):
        current = int(time() * 1000) - self._epo
        if self._ts == current:
            if self._seq == self.MAX_SEQ:
                return None
            self._seq += 1
        else:
            self._seq = 0

        self._ts = current
        return self._ts << 23 | self._inf << 10 | self._seq


short_url = KGenerator(epoch=EPOCH_TIME, instance=INSTANCE_GEN_ID)
uuid = UuidGenerator(epoch=EPOCH_TIME, instance=INSTANCE_GEN_ID)


class GenShortUrl:

    def generate(self):
        counter = next(short_url)
        return base62.encode(counter)
