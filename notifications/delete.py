from pynamodb.exceptions import DoesNotExist, DeleteError
from .models import Notification

def hard_delete_notification(message_id):
    """
    Will delete the row in dynamodb
    """
    try:
        notification = Notification.query(message_id).next()
        notification.delete()
        return True
    except DoesNotExist:
        raise ValueError
    except DeleteError:
        raise ValueError
