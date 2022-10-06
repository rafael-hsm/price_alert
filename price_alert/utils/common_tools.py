import logging

from time import sleep

import schedule

logging.basicConfig(level=logging.INFO, filename='main.log',
                    format='%(asctime)s :: %(levelname)s :: %(lineno)d :: %(funcName)s :: %(message)s :: %(filename)s',
                    datefmt='%d-%b%y %H:%M:%S')


def header(msg: str):
    print('=' * 60)
    print(msg.center(60))
    print('=' * 60)


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end=' ')
        sleep(1)
        num_of_secs -= 1


def footer(msg='Waiting for new request'):
    return msg.center(60)


def schedule_function(function, time_seconds):
    try:
        schedule.every(time_seconds).seconds.do(function)
        while True:
            schedule.run_pending()
    except KeyboardInterrupt:
        print('User stop the script!')


