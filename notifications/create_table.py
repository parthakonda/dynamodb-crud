import logging
from .models import Notification, get_model

def create_table_if_not_exist():
    """
    Will creates the table if not exists
    @return: True/False
    """
    if not Notification.exists():
        try:
            Notification.create_table(read_capacity_units=10, write_capacity_units=10, wait=True)
        except Exception as e:
            logging.error(str(e))
            return False
    return True


def create_dynamic_table_if_not_exist(table_name):
    """
    Will creates the table if not exists
    @return: True/False
    """
    MyNotification = get_model(table_name)
    if not MyNotification.exists():
        try:
            MyNotification.create_table(read_capacity_units=10, write_capacity_units=10, wait=True)
        except Exception as e:
            logging.error(str(e))
            return False
    return True