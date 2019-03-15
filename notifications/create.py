import logging
import uuid
from datetime import datetime
from .models import Notification

def create():
    """
    To insert an entry in dynamodb
    """
    payload = {
        'message_id': str(uuid.uuid4()),
        'from_user': 'parthasaradhi1992@gmail.com',
        'to_user': 'parthasaradhi1992@gmail.com',
        'created_at': datetime.now(),
        'status': 'UNREAD',
        'data': {},
        'message': 'Record Created Successfully',
        'message_type': 'CONTACTS',
        'reference_link': 'NA',
        'exec_status': 'Success',
        'is_deleted': False
    }
    try:
        notification = Notification(**payload)
        notification.save()
        return notification
    except Exception as e:
        logging.error(str(e))
    return None