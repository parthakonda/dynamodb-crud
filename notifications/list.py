import base64
import json
from .models import Notification

def list_all():
    results = Notification.scan()
    results = [item.attribute_values for item in results]
    return results

def list_filter():
    results = Notification.scan(Notification.exec_status == 'Success' & Notification.created_at > 1)
    results = [item.attribute_values for item in results]
    return results

def list_filter_dynamic():
    key, value = 'exec_status', 'Success'
    condition1 = (getattr(Notification, key) == value)
    condition2 = (getattr(Notification, 'from_user') == 'parthasaradhi1992@gmail.com')
    condition = condition1 & condition2
    results = Notification.scan(condition)
    results = [item.attribute_values for item in results]
    return results

def list_filter_limit(limit, last_evaluated_key=None):
    # Note: Currenly only forward pagination is only supported
    if last_evaluated_key is not None:
        _last_evaluated_key = base64.b64decode(last_evaluated_key)
        last_evaluated_key = json.loads(_last_evaluated_key)
    _results = Notification.scan(limit=limit, last_evaluated_key=last_evaluated_key)
    results = [item.attribute_values for item in _results]
    _last_evaluated_key = _results.last_evaluated_key
    if _last_evaluated_key is not None:
        _last_evaluated_key = json.dumps(_last_evaluated_key, sort_keys=True).encode('ascii')
        _last_evaluated_key = base64.b64encode(_last_evaluated_key)
    return {
        'results': results,
        'last_evaluated_key': _last_evaluated_key
    }

def get_unread_count():
    Notification.count(Notification.status == 'UNREAD')
