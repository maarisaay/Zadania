import argparse
import datetime
from enum import Enum
from typing import (
    List,
)

import pandas as pd

from merxu_pim_model.data_objects.translator_language_code import TranslatorLanguage

from src.file_reader.consts import STANDARD_COLUMNS

TRANSLATOR_TARGET_LANGUAGES = [
    TranslatorLanguage.en,
    TranslatorLanguage.pl,
    TranslatorLanguage.et,
    TranslatorLanguage.lt,
    TranslatorLanguage.sk,
    TranslatorLanguage.cs,
    TranslatorLanguage.de,
    TranslatorLanguage.hu,
    TranslatorLanguage.ro,
    TranslatorLanguage.lv
]


def prepare_standard_columns():
    return STANDARD_COLUMNS


def get_descriptive_attributes_columns(df: pd.DataFrame, ignore_columns: List[str] = []):
    standard_columns = prepare_standard_columns()
    return [c for c in df.columns if c and isinstance(c, str) and
            c.split('-')[0] not in standard_columns + ignore_columns]


def prepare_next_daily_run(hour: int, minute: int = 0, second: int = 0):
    date_now = datetime.date.today()
    my_time = datetime.time(hour, minute, second)
    next_run_time = datetime.datetime.combine(date_now, my_time)

    if next_run_time < datetime.datetime.now():
        return next_run_time + datetime.timedelta(hours=24)

    return next_run_time


class UploadSource(Enum):
    DASHBOARD_FILE = 'DASHBOARD_FILE'
    OFFERS_SCHEDULER = 'OFFERS_SCHEDULER'
    DASHBOARD_FORM = 'DASHBOARD_FORM'
    API = 'API'
    BASELINKER = 'BASELINKER'
    UNDEFINED = "UNDEFINED"
    ADMIN = "ADMIN"


def get_arguments(allowed_subscriptions):
    cli = argparse.ArgumentParser('image-downloader',
                                  description="tool for downloading images and uploading to storage")
    cli.add_argument("subscription", choices=allowed_subscriptions)

    return cli.parse_args()

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




