# To store the models
__author__ = 'Partha Saradhi Konda<parthasaradhi1992@gmail.com>'
from pynamodb.models import Model
from datetime import datetime
from pynamodb.attributes import UnicodeAttribute, JSONAttribute, UTCDateTimeAttribute, BooleanAttribute

# Purpose of this model is to store the notifications
# Note: You can have only one hash_key and one range_key MAX
class Notification(Model):
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
