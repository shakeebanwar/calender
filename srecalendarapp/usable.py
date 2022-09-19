from datetime import timedelta,datetime


def expireCalculate():
    date_now_more_30_days = (datetime.now() + timedelta(days=30) )
    return date_now_more_30_days
