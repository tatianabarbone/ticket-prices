from datetime import datetime
import pytz

def get_datetime():
    """
    Returns a tuple containing the current date and time in CST.
    """
    tz = pytz.timezone('US/Central')
    austin_now = str(datetime.now(tz))

    day = austin_now[:10]
    cur_time = austin_now[11:16]

    return (day, cur_time)
