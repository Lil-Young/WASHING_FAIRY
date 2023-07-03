from datetime import datetime
from pymongo import IndexModel, DESCENDING, ASCENDING
from bson.objectid import ObjectId
from .base import Model


class Symbol(Model):

    VERSION = 1

    @property
    def index(self) -> list:
        return [
            IndexModel([('id', ASCENDING)], unique=True),
            IndexModel([('oauth_id', ASCENDING)]),
        ]

    @property
    def schema(self) -> dict:
        return {
            'user_id': None,
            'user_device_token': None,
            'content': None,
            'type': None,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            '__version__': self.VERSION,
        }

    def insert_symbol(self, document: dict):
        return self.col.insert_one(self.schemize(document))

    def get_symbol_one(self, notification_oid: ObjectId):
        return self.col.find_one(
            {'_id': notification_oid},
        )

    def get_symbol(self, skip: int, limit: int):
        return list((
            self.col.find({'type': "공지사항"})
            .sort('updated_at', DESCENDING)
            .skip(skip)
            .limit(limit)
        ))

    def get_user_symbol(self, user_oid: ObjectId, skip: int, limit: int):
        return list((
            self.col.find({'user_id': user_oid,})
            .sort('updated_at', DESCENDING)
            .skip(skip)
            .limit(limit)
        ))

    def delete_symbol(self, notification_oid: ObjectId):
        return self.col.delete_one(
            {'_id': notification_oid}
        )