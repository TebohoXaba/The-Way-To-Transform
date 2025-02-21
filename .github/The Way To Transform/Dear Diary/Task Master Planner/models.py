from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from marshmallow import Schema, fields, validate, post_load

@dataclass
class User:
    username: str
    password: str
    id: Optional[int] = None

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }

@dataclass
class Entry:
    title: str
    content: str
    type: str
    date: datetime
    user_id: int
    completed: bool = False
    id: Optional[int] = None

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'type': self.type,
            'date': self.date.isoformat() if isinstance(self.date, datetime) else self.date,
            'completed': self.completed,
            'user_id': self.user_id
        }

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class EntrySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    type = fields.Str(required=True, validate=validate.OneOf(['task', 'appointment']))
    date = fields.DateTime(required=True, format='%Y-%m-%dT%H:%M')
    completed = fields.Bool(missing=False)
    user_id = fields.Int(required=True)

    @post_load
    def make_entry(self, data, **kwargs):
        return Entry(**data)