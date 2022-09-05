from datetime import datetime

from mongoengine import Document, fields

from apps.constants import EXPIRE_SHORT_URL


class ShortUrl(Document):
    origin_url = fields.StringField(max_length=511, db_index=True)
    short_url = fields.StringField(max_length=15, unique=True, db_index=True)
    created_at = fields.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    expired_at = fields.DateTimeField(default=datetime.now() + EXPIRE_SHORT_URL)

    meta = {'collection': 'short_url'}
