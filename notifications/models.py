# To store the models
__author__ = 'Partha Saradhi Konda<parthasaradhi1992@gmail.com>'
from pynamodb.models import Model
from datetime import datetime
from pynamodb.attributes import UnicodeAttribute, JSONAttribute, UTCDateTimeAttribute, BooleanAttribute, NumberAttribute
from .indexes import ViewIndex

def current_datetime():
    current_datetime = datetime.now()
    created_at = int((current_datetime - datetime(1970, 1, 1)).total_seconds())
    return created_at

# Purpose of this model is to store the notifications
# Note: You can have only one hash_key and one range_key MAX
class Notification(Model):
    message_id = UnicodeAttribute(hash_key=True)
    from_user = UnicodeAttribute()
    to_user = UnicodeAttribute()
    created_at = NumberAttribute(default=current_datetime, range_key=True)
    status = UnicodeAttribute()
    data = JSONAttribute(null=True)
    message = UnicodeAttribute()
    message_type = UnicodeAttribute()
    reference_link = UnicodeAttribute(null=True)
    exec_status = UnicodeAttribute(null=True)
    is_deleted = BooleanAttribute(default=False)
    view_index = ViewIndex()

    class Meta:
        table_name = 'Notification'

    @staticmethod
    def setup_model(model, table_name):
        model.Meta.table_name = table_name


def get_model(table_name):
    """
    This is to set the table_name dynamically
    """
    class MyNotification(Model):
        message_id = UnicodeAttribute(hash_key=True)
        from_user = UnicodeAttribute()
        to_user = UnicodeAttribute()
        created_at = UTCDateTimeAttribute(default=datetime.now, range_key=True)
        status = UnicodeAttribute()
        data = JSONAttribute(null=True)
        message = UnicodeAttribute()
        message_type = UnicodeAttribute()
        reference_link = UnicodeAttribute(null=True)
        exec_status = UnicodeAttribute(null=True)
        is_deleted = BooleanAttribute(default=False)

        class Meta:
            table_name = 'Notification'

        @staticmethod
        def setup_model(model, table_name):
            setattr(model.Meta, 'table_name', table_name)

    MyNotification.setup_model(MyNotification, table_name)
    return MyNotification
