from pynamodb.exceptions import DoesNotExist
from .models import Notification

def read_notification(message_id):
    """
    Will set the notification `status` to 'READ'
    """
    try:
        notification = Notification.query(message_id).next()
        notification.status = 'READ'
        notification.save()
        return notification.attribute_values
    except DoesNotExist:
        raise ValueError


def un_read_notification(message_id):
    """
    Will set the notification `status` to 'UNREAD'
    """
    try:
        notification = Notification.query(message_id).next()
        notification.status = 'UNREAD'
        notification.save()
        return notification.attribute_values
    except DoesNotExist:
        raise ValueError


def delete_notification(message_id):
    """
    Will set the notification `is_deleted` to True
    """
    try:
        notification = Notification.query(message_id).next()
        notification.is_deleted = True
        notification.save()
        return notification.attribute_values
    except DoesNotExist:
        raise ValueError


def archive_notifications():
    notifications = Notification.scan(Notification.status == 'READ')
    for item in notifications:
        item.update(actions=[Notification.status.set('UNREAD')])
