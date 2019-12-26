import psutil
import datetime
import socket

def get_machine_name():
    """
    Gets the machine name
    """
    return socket.getfqdn()

def get_cpu():
    """
    Gets the machine CPU percentage
    """
    return psutil.cpu_percent()

def get_utc_timestamp():
    """
    Gets the UTC timestamp
    """

    now = datetime.datetime.utcnow()
    return now.strftime('%Y-%m-%dT%H:%M:%SZ')

def get_metric_object():
    """
    Gets a metric object as JSON
    """

    MEASUREMENT='metrics'

    return [
    {
        "measurement": MEASUREMENT,
        "tags": {
            "machine": get_machine_name(),
        },
        "time": get_utc_timestamp(),
        "fields": {
            "cpu": get_cpu()
        }
    }
]