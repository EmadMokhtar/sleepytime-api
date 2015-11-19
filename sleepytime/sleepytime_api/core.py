import datetime

def calculate_bed_times(wake_up_time):
    """
    Calculate perfect times to go to bed
    if you want to wake up on certain time
    """
    bed_times = []
    for i in range(1,7):
        bed_time = wake_up_time - datetime.timedelta(minutes=(90*i))
        bed_times.append(bed_time.time())

    return bed_times


def calculate_wakeup_times(bed_time):
    """
    Calculate perfect times to go to bed
    if you want to wake up on certain time
    """
    wakeup_times = []
    for i in range(1,7):
        wakeup_time = bed_time + datetime.timedelta(minutes=(90*i))
        wakeup_times.append(wakeup_time.time())

    return wakeup_times