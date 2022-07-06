import datetime
from datetime import timedelta

def prepare_next_run_time(time: datetime.datetime, start_work_hour: int,  stop_work_hour: int) -> datetime.datetime:
    if time.weekday()==4:
        hours = start_work_hour - time.hour
        next_working_day = time + timedelta(days=3, hours=hours) - timedelta(minutes=time.minute, seconds=time.second)
    elif time.weekday()==5:
        hours = start_work_hour - time.hour
        next_working_day = time + timedelta(days=2, hours=hours) - timedelta(minutes=time.minute, seconds=time.second)
    else:
        if time.hour >= stop_work_hour:
            hours = start_work_hour - time.hour
            next_working_day = time + timedelta(days=2, hours=hours) - timedelta(minutes=time.minute, seconds=time.second)
        else:
            next_working_day = time + timedelta(days=1)

    return print(next_working_day)

prepare_next_run_time(datetime.datetime(2022,7,4,15,26,0),8,16)



