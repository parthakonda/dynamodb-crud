import logging
import uuid
import time
from datetime import datetime
from .models import Notification, current_datetime



def create():
    """
    To insert an entry in dynamodb
    """
    for i in range(1, 20):
        payload = {
            'message_id': str(uuid.uuid4()),
            'from_user': 'parthasaradhi1992@gmail.com',
            'to_user': 'parthasaradhi1992@gmail.com',
            'created_at': current_datetime(),
            'status': 'UNREAD',
            'data': {},
            'message': 'Record Created Successfully {}'.format(i),
            'message_type': 'CONTACTS',
            'reference_link': 'NA',
            'exec_status': 'Success',
            'is_deleted': False
        }
        try:
            notification = Notification(**payload)
            notification.save()
            time.sleep(1)
        except Exception as e:
            logging.error(str(e))
    return None