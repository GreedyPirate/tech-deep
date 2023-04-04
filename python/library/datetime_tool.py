import time
import datetime as dt

def datetime_values():
    # 标准格式时间
    now = dt.datetime.now()
    print(now)

    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.microsecond)
    print("星期", now.weekday() + 1)
    print("星期", now.isoweekday())


def timestamp():
    # 获取时间戳
    mill_timestamp = time.time()
    print(mill_timestamp)

    second_timestamp = int(mill_timestamp)
    print(second_timestamp)

    # 通过时间戳构建
    now = dt.datetime.fromtimestamp(mill_timestamp)


def format_dt():
    # 字符串的解析和反解析
    now = dt.datetime.now()
    pattern = "%Y-%m-%d at %H:%M:%S"
    format_str = now.strftime(pattern)
    print("format date time", format_str)

    parsed_dt = dt.datetime.strptime(format_str, pattern)
    print("parse from string", parsed_dt)


def calc_duration():
    date1 = "2023-03-21 13:10"
    date2 = "2023-01-12 21:32"
    pattern = "%Y-%m-%d %H:%M"

    datetime1 = dt.datetime.strptime(date1, pattern)
    datetime2 = dt.datetime.strptime(date2, pattern)

    delta = datetime1 - datetime2
    print('相差天数', delta.days)
    print('相差秒数', delta.seconds)


if "__main__" == __name__ :
    datetime_values()
    timestamp()
    format_dt()
    calc_duration()

