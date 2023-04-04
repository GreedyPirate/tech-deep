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

if "__main__" == __name__ :
    datetime_values()
    timestamp()
    format_dt()

