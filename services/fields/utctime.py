from datetime import datetime
import calendar


def get_current_utc_time():
    """
    Возвращает текущее время в формате utc
    """
    current_date_time = datetime.utcnow()
    utc_time = calendar.timegm(current_date_time.utctimetuple())
    return utc_time
