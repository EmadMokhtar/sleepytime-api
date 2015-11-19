from django.test import TestCase
from core import calculate_bed_times, calculate_wakeup_times
import datetime

class TestCalculatingBedTimes(TestCase):

    def test_calculate_bed_time_0_minute(self):
        wake_up_time = datetime.datetime(100, 1, 1, 12, 0 , 0)
        bed_time = calculate_bed_times(wake_up_time)
        expected_times = (wake_up_time - datetime.timedelta(minutes=90)).time()

        self.assertEqual(bed_time[0], expected_times)

    def test_calculate_bed_time_45_minute_time(self):
        wake_up_time = datetime.datetime(100, 1, 1, 12, 45 , 0)
        bed_time = calculate_bed_times(wake_up_time)
        expected_times = (wake_up_time - datetime.timedelta(minutes=90)).time()

        self.assertEqual(bed_time[0], expected_times)

    def test_calculate_bed_time_15_minute_time(self):
        wake_up_time = datetime.datetime(100, 1, 1, 12, 15 , 0)
        bed_time = calculate_bed_times(wake_up_time)
        expected_times = (wake_up_time - datetime.timedelta(minutes=90)).time()

        self.assertEqual(bed_time[0], expected_times)


class TestCalculatingWakeUp(TestCase):

    def test_calculate_wakeup_0_minute(self):
        bed_time = datetime.datetime(100, 1, 1, 13, 00, 00)
        wakeup_times = calculate_wakeup_times(bed_time)
        excepted_wake_time = (bed_time + datetime.timedelta(minutes=90)).time()

        self.assertEqual(wakeup_times[0], excepted_wake_time)

    def test_calculate_wakeup_45_minute(self):
        bed_time = datetime.datetime(100, 1, 1, 13, 45, 00)
        wakeup_times = calculate_wakeup_times(bed_time)
        excepted_wake_time = (bed_time + datetime.timedelta(minutes=90)).time()

        self.assertEqual(wakeup_times[0], excepted_wake_time)

    def test_calculate_wakeup_15_minute(self):
        bed_time = datetime.datetime(100, 1, 1, 13, 15, 00)
        wakeup_times = calculate_wakeup_times(bed_time)
        excepted_wake_time = (bed_time + datetime.timedelta(minutes=90)).time()

        self.assertEqual(wakeup_times[0], excepted_wake_time)