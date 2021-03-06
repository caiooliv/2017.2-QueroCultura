from mongoengine import Document
from mongoengine import DictField
from mongoengine import StringField
from mongoengine import DateTimeField
from mongoengine import URLField
from mongoengine import IntField


class Marker(Document):
    platform_id = IntField(required=True)
    name = StringField(required=True)
    marker_type = StringField(required=True)
    action_type = StringField(required=True)
    action_time = DateTimeField(required=True)
    city = StringField(default=None)
    state = StringField(default=None)
    single_url = URLField(default='')
    subsite = IntField(default=None)
    instance_url = StringField(required=True)
    create_time_stamp = DateTimeField(default=None)
    update_time_stamp = DateTimeField(default=None)
    location = DictField(required=True)


class LastRequest(Document):
    date = DateTimeField(required=True)


class Subsite(Document):
    subsite_id = IntField(required=True)
    url = StringField(required=True)
