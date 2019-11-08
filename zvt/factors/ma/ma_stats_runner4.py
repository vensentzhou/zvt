# -*- coding: utf-8 -*-
import logging

from apscheduler.schedulers.background import BackgroundScheduler

from zvt import init_log
from zvt.factors.ma.common import cal_ma_states

logger = logging.getLogger(__name__)

sched = BackgroundScheduler()


@sched.scheduled_job('cron', hour=19, minute=30)
def run1():
    cal_ma_states(start='600000', end='600200')


@sched.scheduled_job('cron', hour=20, minute=0)
def run2():
    cal_ma_states(start='600200', end='601000')


if __name__ == '__main__':
    init_log('ma_stats_runner4.log')

    run1()
    run2()

    sched.start()

    sched._thread.join()